"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from allauth.account.decorators import secure_admin_login

from config.types import EnvironmentTypes

from grumpy.core.urls import urlpatterns as core_urlpatterns
from grumpy.users.urls import urlpatterns as users_urlpatterns
from grumpy.books.urls import urlpatterns as books_urlpatterns
from grumpy.meetings.urls import urlpatterns as meetings_urlpatterns

#########
# admin #
#########

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

#################
# api / swagger #
#################

# TODO ?

#################
# normal routes #
#################

admin.autodiscover()
admin.site.login = secure_admin_login(
    admin.site.login
)  # (just use the same login method for the admin)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include(core_urlpatterns)),
    path("users/", include(users_urlpatterns)),
    path("books/", include(books_urlpatterns)),
    path("meetings/", include(meetings_urlpatterns)),
]

# local static & media files...
if settings.ENVIRONMENT == EnvironmentTypes.DEVELOPMENT:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

if settings.DEBUG:

    # TODO: error pages
    # TODO: profiling pages

    pass
