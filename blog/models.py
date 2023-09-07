from io import BytesIO
from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField

from common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(_("Title"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class SubCategory(BaseModel):
    category = models.ForeignKey(
        Category, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    title = models.CharField(_("Title"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Sub-Category")
        verbose_name_plural = _("Sub-Categories")


class Post(BaseModel):
    title = models.CharField(_("Title"), max_length=100)
    overview = models.TextField(_("Overview"), default="")
    content = HTMLField(_("Content"), default="<p>Hello World</p>")
    featured = models.BooleanField(_("Featured"), default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    thumbnail = models.ImageField(
        _("Thumbnail"), upload_to="thumbnail", default="testing.jpeg", blank=True
    )
    slug = models.CharField(_("Slug"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        """Update URL for Post"""
        return reverse("post_update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        """Delete URL for Post"""
        return reverse("post_delete", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        created_at_str = self.created_at.strftime("%Y-%m-%d")
        self.slug = slugify(self.title, created_at_str)
        super().save(*args, **kwargs)
        if self.thumbnail:
            img = Image.open(default_storage.open(self.thumbnail.name))
            if img.height > 1080 or img.width > 1920:  # pragma:no cover
                output_size = (1920, 1080)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.thumbnail.name, buffer)


class Comment(BaseModel):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    content = models.TextField(_("Content"))
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Newsletter(BaseModel):
    email = models.EmailField(_("Email"), max_length=254)

    class Meta:
        verbose_name = _("Newsletter")
        verbose_name_plural = _("Newsletters")

    def __str__(self):
        return self.email
