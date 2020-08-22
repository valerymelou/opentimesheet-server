import pytest

from opentimesheet.accounts.models import Account
from opentimesheet.accounts.tests.factories import AccountFactory
from opentimesheet.org.models import Organization
from opentimesheet.org.tests.factories import OrganizationFactory
from opentimesheet.users.models import User
from opentimesheet.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def account() -> Account:
    return AccountFactory()


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def org() -> Organization:
    return OrganizationFactory()
