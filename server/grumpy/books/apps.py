from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BooksConfig(AppConfig):
    name = "grumpy.books"
    verbose_name = _("Grumpy Books")

    def ready(self):

        try:
            # register any checks...
            import grumpy.books.checks
        except ImportError:
            pass

        try:
            # register any signals...
            import grumpy.books.signals
        except ImportError:
            pass
