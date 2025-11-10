"""
Custom settings for "development" environment
"""

from .base import *

#########
# setup #
#########

env = environ.Env()

DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY", default="shhh")

########
# apps #
########

# TODOD: might want to insert `whitenoise.runserver_nostatic` to the head of INSTALLED_APPS if I decide to use WhiteNoise in development
# as per https://whitenoise.readthedocs.io/en/latest/django.html#using-whitenoise-in-development

INSTALLED_APPS += []

########################
# static & media Files #
########################

STORAGES = {
    "default": {
        "BACKEND": "grumpy.core.storages.LocalMediaStorage"  # "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "grumpy.core.storages.LocalStaticStorage"  # "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

STATIC_URL = "/static/"
STATIC_ROOT = ROOT_DIR / "_static"

MEDIA_URL = "/media/"
MEDIA_ROOT = ROOT_DIR / "_media"

##################
# security, etc. #
##################

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]
CORS_ALLOW_ALL_ORIGINS = True

#########
# Email #
#########

# in development, just use the console for email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SERVER_EMAIL = PROJECT_EMAIL.format(role="grumpyoldmensbookclub")
DEFAULT_FROM_EMAIL = (
    f"{PROJECT_NAME} <{PROJECT_EMAIL.format(role='grumpyoldmensbookclub')}>"
)

###########
# logging #
###########

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {},
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "colored": {
            "()": "grumpy.core.utils.ColoredFormatter",
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "filters": [],
            "formatter": "colored",
        },
        "mail_admins": {
            "class": "django.utils.log.AdminEmailHandler",
            "filters": [],
            "level": "ERROR",
        },
    },
    "loggers": {
        # change the level of a few particularly verbose loggers
        "django.db.backends": {"level": "WARNING"},
        "django.utils.autoreload": {"level": "INFO"},
    },
    "root": {
        "handlers": [
            "console",
            # "mail_admins",  # don't bother w/ AdminEmailHandler for DEVELOPMENT
        ],
        "level": "DEBUG",
    },
}

#############
# profiling #
#############

import os
import sys

# profiling should be disabled during tests
TESTING = "test" in sys.argv or "PYTEST_VERSION" in os.environ
if not TESTING:

    # see "https://gist.github.com/douglasmiranda/9de51aaba14543851ca3"
    # for tips about making django_debug_toolbar to play nicely w/ Docker
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [
        "127.0.0.1",
        "localhost",
    ] + [ip[:-1] + "1" for ip in ips]

    # add DebugToolbar after staticfile (whitenoise) middleware
    middleware_index = next(
        (
            index
            for index, element in enumerate(MIDDLEWARE)
            if "WhiteNoiseMiddleware" in element
        ),
        None,
    )
    MIDDLEWARE.insert(
        middleware_index + 1 if middleware_index else 0,
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    )

    DEBUG_TOOLBAR_CONFIG = {
        "PROFILER_CAPTURE_PROJECT_CODE": True,
        "SHOW_COLLAPSED": True,
        "SHOW_TOOLBAR_CALLBACK": "debug_toolbar.middleware.show_toolbar_with_docker",
    }

    INSTALLED_APPS += [
        "debug_toolbar",
    ]
