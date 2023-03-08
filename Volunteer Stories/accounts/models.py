import PIL.Image
from io import BytesIO

from rest_framework_simplejwt.tokens import RefreshToken

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.files.storage import default_storage
from django.utils.translation import gettext_lazy as _

from djangoblog.g_models import BaseModel


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, is_user=True, is_volunteer=False, is_admin=False):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)

        user.is_user = is_user
        user.is_volunteer = is_volunteer
        user.is_admin = is_admin

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_user = True
        user.is_volunteer = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, BaseModel, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='email', max_length=60, null=True, blank=True)
    password = models.CharField(max_length=255)
    password_plain = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    picture = models.ImageField(
        _("Picture"),
        upload_to="thumbnail",
        null=True,
        blank=True,
    )
    is_blocked = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = MyUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

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

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class ImageModel(BaseModel):
    image = models.ImageField(_("Image"), upload_to="website_images", blank=True)
    is_hero = models.BooleanField(_("Is hero"), default=False)
    is_divider = models.BooleanField(_("Is divider"), default=False)
    is_gallery = models.BooleanField(_("Is banner"), default=False)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class VolunteerModel(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=15)
    whatsapp = models.CharField(_("Whatsapp Number"), max_length=15)
    social_media = models.CharField(_("Social Media"), max_length=15)
    gender = models.CharField(_("Gender"), max_length=20)
    pronouns = models.CharField(_("Pronouns"), max_length=25)
    date_of_birth = models.DateField(_("Date of Birth"))
    country = models.CharField(_("Country of Residence"), max_length=25)
    nationality = models.CharField(_("Nationality"), max_length=25)
    sector = models.CharField(_("Volunteering Sector"), max_length=255)
    mode_of_communication = models.CharField(
        _("Preferred Mode of Communication"), max_length=50
    )
    photo_sharing_consent = models.BooleanField(_("Photo Sharing Consent"))
    nominee1_name = models.CharField(_("Nominee 1 Name"), max_length=100)
    nominee1_social_media = models.CharField(_("Nominee 1 Social Media"), max_length=50)
    nominee1_country = models.CharField(_("Nominee 1 Country"), max_length=50)
    nominee1_contact = models.CharField(_("Nominee 1 Contact"), max_length=50)
    nominee2_name = models.CharField(_("Nominee 2 Name"), max_length=100)
    nominee2_social_media = models.CharField(_("Nominee 2 Social Media"), max_length=50)
    nominee2_country = models.CharField(_("Nominee 2 Country"), max_length=50)
    nominee2_contact = models.CharField(_("Nominee 2 Contact"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Volunteer")
        verbose_name_plural = _("Volunteers")
