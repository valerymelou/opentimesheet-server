import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class AbstractModel(TimeStampedModel):
    """
    Abstract base class for all models that are not related to an org.
    Provides created and modified fields.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseModel(AbstractModel):
    """
    Abstract base class for all models related to an org.
    Most models in the application will inherit from this class.
    """
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name=_("created by"),
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name=_("modified by"),
        blank=True,
        null=True
    )
    org = models.ForeignKey(
        "org.Organization", on_delete=models.CASCADE, verbose_name=_("organization")
    )

    class Meta:
        abstract = True
