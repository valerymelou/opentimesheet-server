from factory import Faker, SubFactory, post_generation

from opentimesheet.core.tests.factories import BaseFactory
from opentimesheet.users.tests.factories import UserFactory

from ..models import Account


class AccountFactory(BaseFactory):

    user = SubFactory(UserFactory)
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    created_by = SubFactory(UserFactory)

    class Meta:
        model = Account

    @post_generation
    def set_user_org(self, create, extracted, **kwargs):
        # Force the same org on user and account
        self.user.org = self.org
