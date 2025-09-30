from django.urls import include, path

from grumpy.core.views import IndexView

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html")),
    path("", IndexView.as_view()),
]
