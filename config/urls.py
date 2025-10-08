"""
URL configuration for grumpy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

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

admin.autodiscover()
# commented this out to ensure we use the built-in admin login
# rather than allauth's login (to circumvent the approval step)
# admin.site.login = secure_admin_login(
#     admin.site.login
# )

#################
# api / swagger #
#################

# NOT USING DRF

#################
# normal routes #
#################


urlpatterns = [
    # admin...
    path("admin/", admin.site.urls),
    # auth...
    path("accounts/", include("allauth.urls")),
    # apps...
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
