from allauth.account import app_settings
from allauth.account.internal.flows.email_verification import (
    send_verification_email_to_address,
)
from allauth.account.mixins import CloseableSignupMixin
from allauth.account.models import EmailAddress
from allauth.account.views import LoginView as AuthLoginView
from allauth.account.adapter import get_adapter

from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.decorators.http import require_http_methods


class LoginView(CloseableSignupMixin, AuthLoginView):
    """
    Just like the built-in allauth LoginView, except it inherits from CloseableSignupMixin
    which allows disabling of signin just like signup
    """

    template_name_signup_closed = (
        "account/signin_closed." + app_settings.TEMPLATE_EXTENSION
    )

    def is_open(self):
        adapter = get_adapter(self.request)
        return adapter.is_open_for_signin(self.request)


login_view = LoginView.as_view()


@require_http_methods(["POST"])
def reverify_view(request):
    """
    Manually re-verify a user's email address.
    """

    current_user = request.user
    email = request.POST.get("email")

    try:
        emailaddress = EmailAddress.objects.get_for_user(current_user, email)
    except EmailAddress.DoesNotExist:
        raise Http404("Trying to verify an invalid email address")

    if emailaddress.verified:
        msg = f"{email} is already verified."
        messages.add_message(request, messages.INFO, msg)
    else:
        confirmation = send_verification_email_to_address(
            request,
            emailaddress,
            signup=False,
        )

    return HttpResponseRedirect(reverse("users-current"))
