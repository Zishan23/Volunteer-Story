# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Author, Volunteer


class AuthorForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = Author
        fields = ("picture",)


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name")


class VolunteerJoinForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('', 'Select One'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    PRONOUNS_CHOICE = [
        ('', 'Select One'),
        ('he, him, his', 'he, him, his'),
        ('she, her, hers', 'she, her, hers'),
        ('they, them, theirs', 'they, them, theirs'),
        ('Other', 'Other'),
    ]
    SECTOR_CHOICES = [
        ('', 'Select One'),
        ('Education', 'Education'),
        ('Animal Welfare', 'Animal Welfare'),
        ('Transgender Rights', 'Transgender Rights'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Menstrual Hygiene Works', 'Menstrual Hygiene Works'),
        ('Anti-child Labor and Marriage Works', 'Anti-child Labor and Marriage Works'),
        ('Working for Mentally and Physically Challenged', 'Working for Mentally and Physically Challenged'),
        ('Other', 'Other'),
    ]
    MODE_OF_COMMUNICAION_CHOICES = [
        ('', 'Select One'),
        ('Whatsapp', 'Whatsapp'),
        ('Email', 'Email'),
        ('Facebook Messenger', 'Facebook Messenger'),
        ('Phone', 'Phone'),
    ]

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    pronouns = forms.CharField(widget=forms.Select(choices=PRONOUNS_CHOICE))
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    sector = forms.CharField(widget=forms.Select(choices=SECTOR_CHOICES))
    mode_of_communication = forms.CharField(widget=forms.Select(choices=MODE_OF_COMMUNICAION_CHOICES))

    class Meta:
        model = Volunteer
        fields = "__all__"
        exclude = ['created_at', 'updated_at']

    