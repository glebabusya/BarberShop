from config.settings.base import *

DEBUG = True
ALLOWED_HOSTS = []

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

LOCAL_APPS = []

THIRD_PARTY_APPS = [
    "debug_toolbar",
    "rest_framework_swagger",
]

INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS

INTERNAL_IPS = [
    "127.0.0.1",
]
