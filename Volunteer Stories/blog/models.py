from io import BytesIO
from PIL import Image
from tinymce.models import HTMLField

from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from accounts.models import UserModel
from djangoblog.g_models import BaseModel


class CategoryModel(BaseModel):
    title = models.CharField(_("Title"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class SubCategoryModel(BaseModel):
    category = models.ForeignKey(
        CategoryModel, verbose_name=_("Category"), on_delete=models.CASCADE
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
    content = HTMLField(default="<p>Hello World</p>")
    featured = models.BooleanField(_("Featured"), default=False)
    category = models.ForeignKey(
        CategoryModel,
        verbose_name=_("Category"),
        related_name="post",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sub_category = models.ForeignKey(
        SubCategoryModel,
        verbose_name=_("Sub-Category"),
        related_name="post",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    author = models.ForeignKey(
        UserModel, verbose_name=_("Author"), on_delete=models.CASCADE, related_name="post"
    )
    thumbnail = models.ImageField(
        _("Thumbnail"), upload_to="thumbnail", default="testing.jpeg", null=True, blank=True
    )
    slug = models.SlugField(_("Slug"), blank=True, null=True)

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
        self.slug = slugify(self.title, self.created_at)
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
    user = models.ForeignKey(UserModel, verbose_name=_("user"), on_delete=models.CASCADE, related_name="comment")
    content = models.TextField(_("Content"))
    post = models.ForeignKey(
        Post, verbose_name=_("post"), on_delete=models.CASCADE, related_name="comment"
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.user.user.username


class Newsletter(BaseModel):
    email = models.EmailField(_("Email"), max_length=254)

    class Meta:
        verbose_name = _("Newsletter")
        verbose_name_plural = _("Newsletters")

    def __str__(self):
        return self.email
