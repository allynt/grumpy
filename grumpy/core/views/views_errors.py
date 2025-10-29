import logging

from http import HTTPStatus

from django.shortcuts import render

logger = logging.getLogger(__name__)


def bad_request_view(request, exception=None):
    context = {
        "msg": "That was an invalid request.",
    }
    status = HTTPStatus.BAD_REQUEST
    logging.error(f"{status}: {request}")
    return render(request, "error.html", context, status=status)


def permission_denied_view(request, exception=None):
    context = {
        "msg": "You don't have permission to view this resource.",
    }
    status = HTTPStatus.FORBIDDEN
    logging.error(f"{status}: {request}")
    return render(request, "error.html", context, status=status)


def page_not_found_view(request, exception):
    context = {
        "msg": "The requested resource was not found on this server.",
    }
    status = HTTPStatus.NOT_FOUND
    logging.error(f"{status}: {request}")
    return render(request, "error.html", context, status=status)


def error_view(request, exception=None):
    context = {
        "msg": "A server error ocurred.",
    }
    status = HTTPStatus.INTERNAL_SERVER_ERROR
    logging.error(f"{status}: {request}")
    return render(request, "error.html", context, status=status)
