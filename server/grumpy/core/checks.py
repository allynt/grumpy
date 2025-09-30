from django.conf import settings
from django.core.checks import register, Error, Tags


@register(Tags.compatibility)
def check_settings(app_configs, **kwargs):
    """
    Makes sure that some required settings are set as expected.
    """

    errors = []

    properties_to_check = {
        # TODO ?
    }
    for property_name, property_checks in properties_to_check.items():
        try:
            property_value = getattr(settings, property_name)
            for property_check in property_checks:
                assert property_check(property_value)
        except AttributeError:
            errors.append(Error(f"grumpy.core requires '{property_name}' to be set"))
        except (AssertionError, TypeError):
            errors.append(Error(f"'{property_name}' is invalid"))

    return errors
