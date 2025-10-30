from urllib.parse import urljoin

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import MiddlewareNotUsed
from django.shortcuts import redirect


def strip_port_from_domain(domain):
    return domain.split(":", 1)[0]


class DomainRedirectionMiddleware:
    """
    Checks the request domain against the preferred domain.
    Useful for redirecting requests from the hosting's default
    domain to the DNS provider's custom domain.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        if settings.DEBUG:
            raise MiddlewareNotUsed

    def __call__(self, request):
        site = get_current_site(request)
        site_domain = strip_port_from_domain(site.domain)
        request_domain = strip_port_from_domain(request.get_host())

        if request_domain in ["localhost", "127.0.0.1"]:
            return self.get_response(request)

        if request_domain == site_domain:
            return self.get_response(request)
        else:
            url = urljoin(f"{request.scheme}://{site_domain}", request.get_full_path())
            return redirect(url, permanent=True)
