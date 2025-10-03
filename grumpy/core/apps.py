from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from grumpy.core.utils import DynamicSetting


class CoreConfig(AppConfig):
    name = "grumpy.core"
    verbose_name = _("Grumpy Core")

    def ready(self):

        try:
            # register any checks...
            import grumpy.core.checks
        except ImportError:
            pass

        try:
            # register any signals...
            import grumpy.core.signals
        except ImportError:
            pass

        # allow variables defined in django.conf.settings to be instances of DynamicSetting
        DynamicSetting.configure()
