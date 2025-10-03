"""
Custom settings for "deployment" environment.
"""

from .base import *

import logging

logger = logging.getLogger(__name__)

#########
# setup #
#########

env = environ.Env()

DEBUG = env("DJANGO_DEBUG", default="true") == "true"
SECRET_KEY = env("DJANGO_SECRET_KEY")

########
# apps #
########

INSTALLED_APPS += []

#############
# databases #
#############

# Hacky fix for deploymennt; when heroku provision a database,
# it automatically exports `DATABASE_URL` w/ the "postgres" prefix,
# b/c that's automatic, I can't change it...
# even though I've enabled the postgist extensions.
# (the django-on-heroku package could fix this, but that seems a bit heavyweight)`
# So I manually change things here

USE_POSTGIS = env("DJANGO_DATABASE_SCHEME", default="postgres") == "postgis"
logger.info(f"***** USE_POSTGIS = {USE_POSTGIS} *****")
if USE_POSTGIS:
    DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"
    logger.info(
        "overwriting DATABASES['default']['ENGINE'] to support postgis on heroku"
    )
else:
    logger.info("YOU FUCKED UP")

########################
# static & media Files #
########################

# TODO: I'M USING WhiteNoise; SHOULD I USE S3 (VIA Bucketeer) INSTEAD ?

STORAGES = {
    "default": {"BACKEND": "gdjango.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    },
}

STATIC_URL = "/static/"
STATIC_ROOT = ROOT_DIR / "_static"

MEDIA_URL = "/media/"
MEDIA_ROOT = ROOT_DIR / "_media"

##################
# security, etc. #
##################

# ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

#########
# Email #
#########

# TODO

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
