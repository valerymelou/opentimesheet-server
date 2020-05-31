from django.db.models import BooleanField, CharField, ImageField
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from opentimesheet.utils.storages import upload_to


class Organization(TimeStampedModel):
    name = CharField(_("Name"), max_length=100, unique=True)
    logo = ImageField(verbose_name=_("Logo"), upload_to=upload_to, blank=True)
    is_active = BooleanField(
        _("Active"),
        default=True,
        help_text=_("Designates whether this organization should be treated as active"),
    )

    auto_create_schema = True

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name
