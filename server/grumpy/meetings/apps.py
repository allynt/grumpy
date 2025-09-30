from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BooksConfig(AppConfig):
    name = "grumpy.meetings"
    verbose_name = _("Grumpy Meetings")

    def ready(self):

        try:
            # register any checks...
            import grumpy.meetings.checks
        except ImportError:
            pass

        try:
            # register any signals...
            import grumpy.meetings.signals
        except ImportError:
            pass
