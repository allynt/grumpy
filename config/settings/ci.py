"""
Custom settings for "ci" environment.
"""

from .base import *

import logging

logger = logging.getLogger(__name__)

#########
# setup #
#########

env = environ.Env()

DEBUG = False
SECRET_KEY = env("DJANGO_SECRET_KEY", default="shhh")

########
# apps #
########

INSTALLED_APPS += []

#############
# databases #
#############

# no changes needed in ci

########################
# static & media Files #
########################


STORAGES = {
    "default": {"BACKEND": "grumpy.core.storages.LocalMediaStorage"},
    "staticfiles": {"BACKEND": "grumpy.core.storages.LocalStaticStorage"},
}

STATIC_URL = "/static/"
STATIC_ROOT = ROOT_DIR / "_static"

MEDIA_URL = "/media/"
MEDIA_ROOT = ROOT_DIR / "_media"

##################
# security, etc. #
##################

ALLOWED_HOST = env("DJANGO_HOST", default="*")
ALLOWED_HOSTS = [ALLOWED_HOST]
CORS_ALLOW_ALL_ORIGINS = True

#########
# Email #
#########

# in ci, just use the console for email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SERVER_EMAIL = PROJECT_EMAIL.format(role="grumpyoldmensbookclub")
DEFAULT_FROM_EMAIL = (
    f"{PROJECT_NAME} <{PROJECT_EMAIL.format(role='grumpyoldmensbookclub')}>"
)

###########
# logging #
###########

# no logging in ci
