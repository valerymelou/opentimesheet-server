from factory import DjangoModelFactory, Faker

from ..models import Organization


class OrganizationFactory(DjangoModelFactory):

    name = Faker("name")

    class Meta:
        model = Organization
        django_get_or_create = ["name"]
