from django.urls import include, path

from grumpy.core.views import IndexView, ContactView, HelpView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contact", ContactView.as_view(), name="contact"),
    path("help", HelpView.as_view(), name="help"),
    path("captcha", include("captcha.urls")),  # captcha is used for ContactForm
]
