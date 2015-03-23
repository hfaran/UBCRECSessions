#!/usr/bin/env python3

import logging
import os
import time
import signal
import json
import uuid

import click
import tornado.httpserver
import tornado.ioloop
from tornado_json.application import Application

from ubcrec.sqlAPI import SQLAPI
from ubcrec.config import UBCRECConfig
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


@click.command()
@click.option('-p', '--port', default=8888, type=int, required=True,
              help="Port to start server on")
@click.option('--db', default="project.db", type=str, required=True,
              help="Path of database file")
@click.option('--session-timeout-days', default=1, required=True,
              help=("Cookie expiration time in days; can also be set to "
                    "``None`` for session cookies, i.e., cookies that "
                    "expire when browser window is closed."))
@click.option('--cookie-secret', default="", required=True,
              help=("Set this to an empty string to generate a new cookie secret "
                    "each time the server is restarted, or to any string which is "
                    "the cookie secret."))
def main(port, db, session_timeout_days, cookie_secret):
    """
    - Get options from config file
    - Gather all routes
    - Create the server
    - Start the server
    """
    global http_server

    ubcrec_config = UBCRECConfig(
        port=port,
        db_file=db,
        session_timeout_days=session_timeout_days,
        cookie_secret=cookie_secret
    )

    routes = []  # mod_routes.assemble_routes()

    settings = dict(
        template_path=os.path.join(
            os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        gzip=True,
        cookie_secret=(cookie_secret if cookie_secret
                       else uuid.uuid4().hex),
        ubcrec=ubcrec_config
        # login_url="/signin/signin"
    )

    # Create server
    http_server = tornado.httpserver.HTTPServer(
        Application(
            routes=routes,
            settings=settings,
            db_conn=SQLAPI(db),
        )
    )
    # Bind to port
    http_server.listen(port)

    # Register signal handlers for quitting
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    # Start IO loop
    tornado.ioloop.IOLoop.instance().start()

    logging.info("Exit...")


if __name__ == '__main__':
    main()
