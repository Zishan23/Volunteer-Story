from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from blog.models import Category, SubCategory


class Image(models.Model):
    image = models.ImageField(_("Image"), upload_to="website_images", blank=True)
    is_active = models.BooleanField(_("Is active"), default=False)
    is_hero = models.BooleanField(_("Is hero"), default=False)
    is_divider = models.BooleanField(_("Is divider"), default=False)
    is_gallery = models.BooleanField(_("Is banner"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class Volunteer(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=15)
    whatsapp = models.CharField(_("Whatsapp Number"), max_length=25)
    social_media = models.CharField(_("Social Media"), max_length=150)
    gender = models.CharField(_("Gender"), max_length=20)
    pronouns = models.CharField(_("Pronouns"), max_length=25)
    date_of_birth = models.DateField(_("Date of Birth"))
    country = models.CharField(_("Country of Residence"), max_length=25)
    nationality = models.CharField(_("Nationality"), max_length=25)
    sector = models.CharField(_("Volunteering Sector"), max_length=255)
    mode_of_communication = models.CharField(
        _("Preffered Mode of Communication"), max_length=50
    )
    image = models.ImageField(_("Image"), upload_to="volunteer_images", blank=True)
    photo_sharing_consent = models.BooleanField(_("Photo Sharing Consent"))
    nominee1_name = models.CharField(_("Nominee 1 Name"), max_length=100)
    nominee1_social_media = models.CharField(_("Nominee 1 Social Media"), max_length=50)
    nominee1_country = models.CharField(_("Nominee 1 Country"), max_length=50)
    nominee1_contact = models.CharField(_("Nominee 1 Contact"), max_length=50)
    nominee2_name = models.CharField(_("Nominee 2 Name"), max_length=100)
    nominee2_social_media = models.CharField(_("Nominee 2 Social Media"), max_length=50)
    nominee2_country = models.CharField(_("Nominee 2 Country"), max_length=50)
    nominee2_contact = models.CharField(_("Nominee 2 Contact"), max_length=50)
    story_title = models.CharField(max_length=100)
    story_overview = models.TextField(default="")
    story_content = HTMLField()
    story_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=_("Story Category"))
    story_sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, verbose_name=_("Story Sub Category"))
    story_image = models.ImageField(upload_to="story_image")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Volunteer")
        verbose_name_plural = _("Volunteers")
