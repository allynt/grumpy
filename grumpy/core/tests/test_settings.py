import pytest
from . import factories

from grumpy.core.models import GrumpySettings

@pytest.mark.django_db
class TestGrumpySettings:

    def test_settings_is_singleton(self):

        number_of_singletons = GrumpySettings.objects.count()
        assert number_of_singletons == 0
        singleton = GrumpySettings()
        singleton.save()
        singleton2 = GrumpySettings()
        singleton2.save()
        number_of_singletons = GrumpySettings.objects.count()
        assert number_of_singletons == 1
        assert singleton2.id == None
        assert singleton.id != None
