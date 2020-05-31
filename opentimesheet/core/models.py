from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from opentimesheet.org.models import Organization


class BaseModel(TimeStampedModel):
    org = models.ForeignKey(
        Organization, on_delete=models.CASCADE, verbose_name=_("organization")
    )

    class Meta:
        abstract = True
