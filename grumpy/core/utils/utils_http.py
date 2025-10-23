from http import HTTPStatus


def is_informational(status_code):
    status = HTTPStatus(status_code)
    return status.is_informational


def is_success(status_code):
    status = HTTPStatus(status_code)
    return status.is_success


def is_redirection(status_code):
    status = HTTPStatus(status_code)
    return status.is_redirection


def is_client_error(status_code):
    status = HTTPStatus(status_code)
    return status.is_client_error


def is_server_error(status_code):
    status = HTTPStatus(status_code)
    return status.is_server_error


def is_error(status_code):
    return is_client_error(status_code) or is_server_error(status_code)
