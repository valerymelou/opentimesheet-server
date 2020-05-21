from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrgConfig(AppConfig):
    name = "opentimesheet.org"
    verbose_name = _("Org")
