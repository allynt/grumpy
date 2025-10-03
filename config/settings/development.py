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

# TODOD: might want to add `whitenoise.runserver_nostatic` if I decide to use whitenoise in development
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
