from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from opentimesheet.core.models import BaseModel


class Account(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="account",
    )
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    hire_date = models.DateField(_("hire date"), null=True, blank=True)
    release_date = models.DateField(_("release date"), null=True, blank=True)

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def get_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_name()
