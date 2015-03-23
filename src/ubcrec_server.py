#!/usr/bin/env python2.7

import logging
import os
import time
import signal
import json
import uuid
import socket
from urllib import urlretrieve

import jsonpickle
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import options
from tornado_json.application import Application

# from cutthroat import db2
from ubcrec.sqlAPI import SQLAPI
# from cutthroat import ctconfig
# from cutthroat import routes as mod_routes


MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3


def sig_handler(sig, frame):
    """Handles SIGINT by calling shutdown()"""
    logging.warning('Caught signal: %s', sig)
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
    """Waits MAX_WAIT_SECONDS_BEFORE_SHUTDOWN, then shuts down the server"""
    logging.info('Stopping http server')
    http_server.stop()

    logging.info('Will shutdown in %s seconds ...',
                 MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)
    io_loop = tornado.ioloop.IOLoop.instance()

    deadline = time.time() + MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop()
            logging.info('Shutdown')

    stop_loop()


def main():
    """
    - Get options from config file
    - Gather all routes
    - Create the server
    - Start the server
    """
    global http_server

    routes = []  # mod_routes.assemble_routes()
    settings = dict(
        template_path=os.path.join(
            os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        gzip=True,
        cookie_secret=(options.cookie_secret if options.cookie_secret
                       else uuid.uuid4().hex),
        # login_url="/signin/signin"
    )

    # If asked to write routes, do so
    if options.output_routes:
        with open("routes.json", "w+") as f:
            f.write(
                json.dumps(
                    [(route, jsonpickle.encode(rh)) for route, rh in routes],
                    indent=4
                )
            )

    http_server = tornado.httpserver.HTTPServer(
        Application(
            routes=routes,
            settings=settings,
            db_conn=SQLAPI(options.sqlite_db),
        )
    )

    for port in options.ports:
        try:
            logging.debug("Attempting to bind on {}.".format(port))
            http_server.listen(port)
            logging.info("Listening on {}.".format(port))
            break
        except socket.error:
            logging.debug("Could not bind on {}.".format(port))
    else:
        raise Exception("Ran out of ports to try.")

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    tornado.ioloop.IOLoop.instance().start()

    logging.info("Exit...")


if __name__ == '__main__':
    main()
