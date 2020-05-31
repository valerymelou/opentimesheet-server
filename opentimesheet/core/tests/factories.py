from factory import DjangoModelFactory, SubFactory

from opentimesheet.org.tests.factories import OrganizationFactory

from ..models import BaseModel


class BaseFactory(DjangoModelFactory):

    org = SubFactory(OrganizationFactory)

    class Meta:
        model = BaseModel
        abstract = True
