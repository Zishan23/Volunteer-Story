# -*- coding: utf-8 -*-
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.db import models
from django.utils.translation import gettext_lazy as _
import PIL.Image


class Author(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    picture = models.ImageField(
        _("Picture"), upload_to="thumbnail", default="testing.jpeg", null=True, blank=True
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:  # pragma: no cover
            img = PIL.Image.open(default_storage.open(self.picture.name))
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.picture.name, buffer)


class Image(models.Model):
    image = models.ImageField(_("Image"), upload_to="website_images",  blank=True)
    is_active = models.BooleanField(_("Is active"), default=False)
    is_hero = models.BooleanField(_("Is hero"), default=False)
    is_divider = models.BooleanField(_("Is divider"), default=False)
    is_gallery = models.BooleanField(_("Is banner"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
