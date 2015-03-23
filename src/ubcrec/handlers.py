from tornado_json import requesthandlers


class APIHandler(requesthandlers.APIHandler):
    """APIHandler"""

    body = None  # For PyCharm completion, since this is otherwise dynamically
                 # inserted

    def get_current_user(self):
        return self.get_secure_cookie("user")


class ViewHandler(requesthandlers.ViewHandler):
    """ViewHandler"""

    body = None

    def get_current_user(self):
        return self.get_secure_cookie("user")
