from django.urls import resolve as base_resolve
from django.urls import reverse as base_reverse
from rest_framework.settings import api_settings


def reverse(view_name, args=None, kwargs=None):
    view_name = "{0}:{1}".format(api_settings.DEFAULT_VERSION, view_name)
    return base_reverse(view_name, args=args, kwargs=kwargs)


def resolve(path):
    path = "/{0}{1}".format(api_settings.DEFAULT_VERSION, path)
    return base_resolve(path)


def build_view_name(view_name, version=None):
    version = version or api_settings.DEFAULT_VERSION
    return "{0}:{1}".format(version, view_name)


def build_path(path, version=None):
    version = version or api_settings.DEFAULT_VERSION
    return "/{0}{1}".format(version, path)
