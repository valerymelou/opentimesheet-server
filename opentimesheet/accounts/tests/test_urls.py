import uuid

from opentimesheet.core.tests import build_path, build_view_name, resolve, reverse


def test_account_list():
    assert reverse("account-list") == build_path("/accounts/")
    assert resolve("/accounts/").view_name == build_view_name("account-list")


def test_account_detail():
    pk = uuid.uuid4()
    assert reverse("account-detail", kwargs={"pk": pk}) == build_path(
        "/accounts/{0}/".format(pk)
    )
    assert resolve("/accounts/{0}/".format(pk)).view_name == build_view_name(
        "account-detail"
    )
