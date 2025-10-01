from django.contrib import messages

from allauth.account.adapter import DefaultAccountAdapter

from grumpy.users.models import User


def get_user_display(user):
    # https://joshkaramuth.com/blog/django-allauth-without-username-field/
    return user.email

    import typing


class AccountAdapter(DefaultAccountAdapter):
    pass
