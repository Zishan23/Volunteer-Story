from django.contrib.auth.models import User
from tinymce.models import HTMLField
from multiselectfield import MultiSelectField
from blog.models import Category, SubCategory
from io import BytesIO
from django.core.files.storage import default_storage
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from common.models import BaseModel


class ImageModel(BaseModel):
    image = models.ImageField(_("Image"), upload_to="website_images", blank=True)
    is_hero = models.BooleanField(_("Is hero"), default=False)
    is_divider = models.BooleanField(_("Is divider"), default=False)
    is_gallery = models.BooleanField(_("Is banner"), default=False)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class SubmitStoryModel(BaseModel):
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
    story_title = models.CharField(_("Story Title"), max_length=100)
    story_overview = models.TextField(_("Story Overview"), default="")
    story_content = HTMLField(_("Story Content"))
    story_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    story_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    story_image = models.ImageField(_("Story Image"), upload_to="story_image")
    is_reviewed = models.BooleanField(_("Is Reviewed"), default=False)
    is_verified = models.BooleanField(_("Is Verified"), default=False)
    is_published = models.BooleanField(_("Is Published"), default=False)
    reviewed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewed_by", null=True, blank=True
    )
    verified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="verified_by", null=True, blank=True
    )
    published_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="published_by", null=True, blank=True
    )

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")


POST_CHOICES = (
    ("Story Writer", "Story Writer (Write a story from the interview)"),
    ("Interviewer", "Interviewer (Take interview of our guests)"),
    (
        "Graphics Designer",
        "Graphics Designer (Design Social Media Content and Edit Photos and Videos)",
    ),
    (
        "Social Media Officer",
        "Social Media Officer (Handle and Prepare Content for Social Media Platforms of VS)",
    ),
)


class VolunteerJoinModel(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=100)
    gender = models.CharField(_("Gender"), max_length=20)
    date_of_birth = models.DateField(_("Date of Birth"))
    blood_group = models.CharField(_("Blood Group"), max_length=20)
    phone = models.CharField(_("Phone"), max_length=15)
    emergency_contact = models.CharField(_("Emergency Contact"), max_length=15)
    present_address = models.TextField(_("Present Address"))
    permanent_address = models.TextField(_("Permanent Address"))
    social_media = models.CharField(_("Social Media"), max_length=150)
    current_institution = models.CharField(_("Current Institution"), max_length=100)
    department = models.CharField(_("Department"), max_length=100)
    semester = models.CharField(_("Semester"), max_length=100)
    post = MultiSelectField(_("Post"), choices=POST_CHOICES, max_length=100)
    is_experienced = models.BooleanField(_("Is Experienced"), default=False)
    previous_work = models.FileField(
        _("Previous Work"),
        upload_to="volunteer_join_previous_work",
        null=True,
        blank=True,
    )
    work_link = models.CharField(_("Work Link"), max_length=100, null=True, blank=True)
    reason_to_join = models.TextField(_("Reason to Join"))
    extra_curricular_activities = models.TextField(
        _("Extra Curricular Activities"), null=True, blank=True
    )
    got_to_know_us = models.CharField(_("Got to Know Us Via"), max_length=100)
    subscribe_to_newsletter = models.CharField(
        _("Subscribe to Newsletter"), max_length=100
    )

    class Meta:
        verbose_name = _("Volunteer Join")
        verbose_name_plural = _("Volunteer Joins")


class TeamMemberModel(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=100, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=15, null=True, blank=True)
    designation = models.CharField(_("Designation"), max_length=200, null=True, blank=True)
    address = models.TextField(_("Address"), null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to='team_members/', null=True, blank=True)
    serial = models.IntegerField(_("Serial"), default=0)
    description = models.TextField(_("Description"), null=True, blank=True)
    facebook_link = models.URLField(_("Facebook Link"), null=True, blank=True)
    twitter_link = models.URLField(_("Twitter Link"), null=True, blank=True)
    instagram_link = models.URLField(_("Instagram Link"), null=True, blank=True)
    linkedin_link = models.URLField(_("Linkedin Link"), null=True, blank=True)

    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')
        ordering = ['serial']

    def __str__(self):
        return f"{self.name} - {self.designation}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image)
            image.thumbnail((200, 200))
            image_data = BytesIO()
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            image.save(image_data, format="JPEG")
            thumbnail_name = f"thumbnail_{self.image.name}"
            default_storage.save(thumbnail_name, image_data)
            self.thumbnail_image = thumbnail_name
            super().save(*args, **kwargs)
