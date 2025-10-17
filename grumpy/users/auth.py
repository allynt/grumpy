from django import forms
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import mail_managers
from django.urls import reverse
from django.utils.encoding import force_str

from allauth.account import app_settings as auth_app_settings
from allauth.account.adapter import DefaultAccountAdapter


def get_user_display(user):
    # https://joshkaramuth.com/blog/django-allauth-without-username-field/
    return user.email


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return settings.ALLOW_SIGNUP

    def is_open_for_signin(self, request):
        return settings.ALLOW_SIGNIN

    def authenticate(self, request, **credentials):
        user = super().authenticate(request, **credentials)
        if user is not None:
            # add an extra check for authentication...
            if settings.REQUIRE_APPROVAL and not user.is_approved:
                msg = f"{user} has not been approved yet."
                raise forms.ValidationError(msg)
        return user

    def get_password_change_redirect_url(self, request):
        """
        The URL to redirect to after a successful password change/set.
        """
        return reverse("index")

    def format_email_subject(self, subject) -> str:
        """
        Formats the given email subject.
        Overriding the built-in fn to improve formatting a bit
        """
        prefix = auth_app_settings.EMAIL_SUBJECT_PREFIX
        if prefix is None:
            return super().format_email_subject(subject)
        formatted_prefix = "[{name}] ".format(
            name=prefix.strip().lstrip("[").rstrip("]")
        )
        return formatted_prefix + force_str(subject)

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new User instance from the signup form / serializer.
        Overriding to send a notification email.  Using this adapter
        instead of signals so that the notification is only sent when
        a user is added via the signup form (as opposed to the shell or admin).
        """

        saved_user = super().save_user(request, user, form, commit=commit)
        if commit and settings.NOTIFY_SIGNUPS:
            subject = super().format_email_subject(f"new user signup: {saved_user}")
            message = f"User {saved_user.email} signed up for an account at {get_current_site(request)}."
            mail_managers(subject, message, fail_silently=True)

        return saved_user
