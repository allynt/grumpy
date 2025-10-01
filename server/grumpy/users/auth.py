from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model

from allauth.account.adapter import DefaultAccountAdapter

from grumpy.users.models import User


def get_user_display(user):
    # https://joshkaramuth.com/blog/django-allauth-without-username-field/
    return user.email


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return settings.ALLOW_SIGNUP
