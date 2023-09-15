from django.utils.translation import gettext_lazy as _
from django.db import models


class AuditAbstractModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=True,
        verbose_name=_('created on'),
    )
    created_by = models.UUIDField()
    modified = models.DateTimeField(
        auto_now=True,
        editable=False,
        null=True,
        verbose_name=_('modified on'),
    )
    modified_by = models.UUIDField()
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
