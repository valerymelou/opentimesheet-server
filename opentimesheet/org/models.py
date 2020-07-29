import uuid as uuid_lib

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from opentimesheet.utils.storages import upload_to


class Organization(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=100)
    logo = models.ImageField(verbose_name=_("logo"), upload_to=upload_to, blank=True)
    website = models.URLField(_("website"), blank=True)
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this organization should be treated" " as active"
        ),
    )

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
        ordering = ("-created",)

    def __str__(self):
        return self.name
