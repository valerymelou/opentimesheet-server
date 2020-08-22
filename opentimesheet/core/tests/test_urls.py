from opentimesheet.core.tests import build_path, build_view_name, resolve, reverse


def test_api_root():
    assert reverse("api-root") == build_path("/")
    assert resolve("/").view_name == build_view_name("api-root")
