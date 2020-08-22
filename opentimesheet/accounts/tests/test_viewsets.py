import json

from rest_framework import status

from opentimesheet.core.tests import APITestCase, reverse
from opentimesheet.org.tests.factories import OrganizationFactory
from opentimesheet.users.tests.factories import UserFactory

from ..models import Account
from .factories import AccountFactory


class TestAccountViewSet(APITestCase):
    def setUp(self):
        org = OrganizationFactory()
        self.user = UserFactory(org=org)
        self.account1 = AccountFactory(
            first_name="Jane", last_name="Doe", org=self.user.org
        )
        self.account2 = AccountFactory(
            first_name="John", last_name="Doe", org=self.user.org
        )
        AccountFactory(
            first_name="Mike", last_name="Smith"
        )  # Another account but on different org
        self.client.force_authenticate(self.user)

    def test_list(self):
        """
        Ensure we can list accounts.
        """
        url = reverse("account-list")
        response = self.client.get(url)
        self.assertContains(response, "Jane")
        self.assertContains(response, "John")
        self.assertEqual(len(json.loads(response.content)["data"]), 2)

    def test_create(self):
        """
        Ensure we can create an account.
        """
        url = reverse("account-list")
        post = {
            "data": {
                "type": "Account",
                "attributes": {
                    "firstName": "Valery",
                    "lastName": "Melou",
                    "user": {
                        "email": "valery@opentimesheet.com",
                        "password": "password",
                    },
                },
            }
        }
        response = self.client.post(url, post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # TODO: test the content

    def test_detail(self):
        url = reverse("account-detail", kwargs={"pk": self.account1.pk})
        response = self.client.get(url)
        self.assertContains(response, "Jane")

    def test_delete(self):
        url = reverse("account-detail", kwargs={"pk": self.account2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Account.objects.count(), 2)
