from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_tenants.models import DomainMixin, TenantMixin

from opentimesheet.core.models import AbstractModel
from opentimesheet.utils.storages import upload_to


class Organization(TenantMixin, AbstractModel):
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


class Domain(DomainMixin):
    pass
