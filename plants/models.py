import datetime as dt
import uuid
from typing import Optional

from django.db import models
from django.urls import reverse
from djangoyearlessdate.models import YearlessDateField

from .storages import ThumbnailsStorage


def thumbnail_path(instance, filename):
    return uuid.uuid4().hex


class Image(models.Model):
    is_main = models.BooleanField()
    image = models.ImageField(upload_to="plant_images")
    plant = models.ForeignKey(
        "Plant",
        related_name="images",
        related_query_name="image",
        on_delete=models.PROTECT,
    )


class Plant(models.Model):
    # names
    name = models.TextField(unique=True, help_text="Main name, must be unique")
    name_alt = models.TextField(
        null=True,
        blank=True,
        help_text="Alternative name, i.e. in latin or other common names",
    )
    name_en = models.TextField(null=True, blank=True, help_text="Name in English")

    # properties
    when = models.TextField(null=True, blank=True)
    bloom_start = YearlessDateField(null=True, blank=True)
    bloom_end = YearlessDateField(null=True, blank=True)
    collect_start = YearlessDateField(null=True, blank=True)
    collect_end = YearlessDateField(null=True, blank=True)
    where = models.TextField(null=True, blank=True)
    how = models.TextField(null=True, blank=True)
    benefit = models.TextField(null=True, blank=True)
    harm = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(
        storage=ThumbnailsStorage(),
        upload_to=thumbnail_path,
        null=True,
        blank=True,
        help_text="This is the image that will be displayed on each plant card. "
        "Must be square and preferably 200x200 pixels.",
    )

    # cross-references
    plantnet_url = models.URLField(null=True, blank=True)
    gbif_id = models.PositiveIntegerField(null=True, blank=True)
    wikipedia_url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def until(self) -> Optional[int]:
        if not self.bloom_start:
            return None

        today = dt.date.today()
        when = dt.date(today.year, self.bloom_start.month, self.bloom_start.day)

        if when < today:
            return None

        return (when - today).days

    def get_absolute_url(self):
        return reverse("plants:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"
