from django.urls import include, path

from grumpy.core.views import IndexView, HelpView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("help", HelpView.as_view(), name="help"),

]
