import functools
import urllib.parse as urlparse  # py3
from urllib.parse import urlencode  # py3

from tornado.web import HTTPError


def authenticated(user_types):
    """This is a customized version of tornado's authenticated decorator

    :param user_types: A user is only considered logged in if the current
        user_type matches one of the provided in user_types
    :type user_types: str or list
    """
    if isinstance(user_types, str):
        user_types = [user_types]

    def _authenticated(method):
        """Decorate methods with this to require that the user be logged in.

        If the user is not logged in, they will be redirected to the configured
        `login url <RequestHandler.get_login_url>`.

        If you configure a login url with a query parameter, Tornado will
        assume you know what you're doing and use it as-is.  If not, it
        will add a `next` parameter so the login page knows where to send
        you once you're logged in.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if (
                not self.current_user or
                self.user_type not in user_types
            ):
                if self.request.method in ("GET", "HEAD"):
                    url = self.get_login_url()
                    if "?" not in url:
                        if urlparse.urlsplit(url).scheme:
                            # if login url is absolute, make next absolute too
                            next_url = self.request.full_url()
                        else:
                            next_url = self.request.uri
                        url += "?" + urlencode(dict(next=next_url))
                    self.redirect(url)
                    return
                raise HTTPError(403)
            return method(self, *args, **kwargs)
        return wrapper
    return _authenticated
