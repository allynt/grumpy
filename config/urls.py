"""
URL configuration for grumpy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

"""

from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500
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

# errors
handler400 = "grumpy.core.views.bad_request_view"
handler403 = "grumpy.core.views.permission_denied_view"
handler404 = "grumpy.core.views.page_not_found_view"
handler500 = "grumpy.core.views.error_view"

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

    # error pages...
    from functools import partial
    from importlib import import_module
    from django.http import (
        HttpResponseBadRequest,
        HttpResponseForbidden,
        HttpResponseNotFound,
    )
    from grumpy.core.utils import import_callable

    urlpatterns += [
        path(
            "400/",
            partial(import_callable(handler400), exception=HttpResponseBadRequest()),
        ),
        path(
            "403/",
            partial(import_callable(handler403), exception=HttpResponseForbidden()),
        ),
        path(
            "404/",
            partial(import_callable(handler404), exception=HttpResponseNotFound()),
        ),
        path("500/", partial(import_callable(handler500), exception=None)),
    ]

    # TODO: profiling pages...

    pass
