from django.urls import resolve, reverse


def test_api_root():
    assert reverse("api:api-root") == "/"
    assert resolve("/").view_name == "api:api-root"
