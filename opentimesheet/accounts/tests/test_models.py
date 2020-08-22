import pytest

from ..models import Account

pytestmark = pytest.mark.django_db


class TestAccount:
    def test_get_name(self, account: Account):
        assert account.get_name() == "{0} {1}".format(
            account.first_name, account.last_name
        )

    def test__str__(self, account: Account):
        assert account.__str__() == "{0} {1}".format(
            account.first_name, account.last_name
        )
