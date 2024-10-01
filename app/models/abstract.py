import datetime as dt
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    """Timestamp model"""

    created_at: dt.datetime = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at")
    )
    changed_at: dt.datetime = models.DateTimeField(
        auto_now=True, verbose_name=_("Changed at")
    )

    @property
    def created_at_pretty(self):
        return self.created_at.strftime("%d.%m.%Y %H:%M:%S")

    @property
    def changed_at_pretty(self):
        return self.changed_at.strftime("%d.%m.%Y %H:%M:%S")

    class Meta:
        abstract = True
