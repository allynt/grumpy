from allauth.account import app_settings
from allauth.account.mixins import CloseableSignupMixin
from allauth.account.views import LoginView as AuthLoginView
from allauth.account.adapter import get_adapter

"""
Overridding the built-in allauth login view so that it can be disabled
"""


class LoginView(CloseableSignupMixin, AuthLoginView):
    """
    Just like the built-in allauth LoginView, except it inherits from CloseableSignupMixin
    which allows disabling of signin just like signup
    """

    template_name_signup_closed = (
        "account/signin_closed." + app_settings.TEMPLATE_EXTENSION
    )

    def is_open(self):
        return get_adapter(self.request).is_open_for_signin(self.request)


login_view = LoginView.as_view()
