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

INSTALLED_APPS += []

########################
# static & media Files #
########################

STATICFILES_STORAGE = "grumpy.core.storage.LocalStaticStorage"
DEFAULT_FILE_STORAGE = "grumpy.core.storage.LocalMediaStorage"

STATIC_URL = "/static/"
STATIC_ROOT = ROOT_DIR / "_static"

MEDIA_URL = "/media/"
MEDIA_ROOT = ROOT_DIR / "_media"

# These next env vars aren't used in development, but they still ought
# to be defined so that the classes in "storages.py" module can load...

STATIC_LOCATION = ""
STATIC_DEFAULT_ACL = ""
PUBLIC_MEDIA_LOCATION = ""
PUBLIC_MEDIA_DEFAULT_ACL = ""
PRIVATE_MEDIA_LOCATION = ""
PRIVATE_MEDIA_DEFAULT_ACL = ""

##################
# security, etc. #
##################

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

#########
# Email #
#########

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

#######
# API #
#######

# TODO ?

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
