from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "grumpy.users"
    verbose_name = _("Grumpy Users")

    def ready(self):

        try:
            # register any checks...
            import grumpy.users.checks
        except ImportError:
            pass

        try:
            # register any signals...
            import grumpy.users.signals
        except ImportError:
            pass
