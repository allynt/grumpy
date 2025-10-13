import factory
from factory.faker import (
    Faker as FactoryFaker,
)  # note I use FactoryBoy's wrapper of Faker
from grumpy.core.models import GrumpySettings


class GrumpySettingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GrumpySettings

    allow_signin = FactoryFaker("boolean")
    allow_signup = FactoryFaker("boolean")
    require_approval = FactoryFaker("boolean")

    # just accept the default values of other fields
