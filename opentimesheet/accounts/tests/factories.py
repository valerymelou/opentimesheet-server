from factory import Faker, SubFactory

from opentimesheet.core.tests.factories import BaseFactory
from opentimesheet.users.tests.factories import UserFactory

from ..models import Account


class AccountFactory(BaseFactory):

    user = SubFactory(UserFactory)
    first_name = Faker("first_name")
    last_name = Faker("last_name")

    class Meta:
        model = Account
