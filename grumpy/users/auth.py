from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model

from allauth.account.adapter import DefaultAccountAdapter


def get_user_display(user):
    # https://joshkaramuth.com/blog/django-allauth-without-username-field/
    return user.email


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return settings.ALLOW_SIGNUP

    def authenticate(self, request, **credentials):
        user = super().authenticate(request, **credentials)
        if user is not None:
            # add an extra check for authentication...
            if settings.REQUIRE_APPROVAL and not user.is_approved:
                msg = f"{user} has not been approved yet."
                raise forms.ValidationError(msg)
        return user
