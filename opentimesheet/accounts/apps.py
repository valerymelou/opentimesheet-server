from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountsConfig(AppConfig):
    name = "opentimesheet.accounts"
    verbose_name = _("Accounts")