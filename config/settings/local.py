import mimetypes

from .base import *

DEBUG = True
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS += [
    "debug_toolbar",
]

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

#DJANGO_SETTINGS_MODULE = "config.settings.local"


def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    "INTERCEPT_REDIRECTS": False,
}
