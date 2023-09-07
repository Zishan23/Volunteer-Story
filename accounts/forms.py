from django import forms
from accounts.models import *
from tinymce.widgets import TinyMCE

GENDER_CHOICES = [
    ("", "Select One"),
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]

BLOOD_GROUP_CHOICES = [
    ("", "Select One"),
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
]

GOT_TO_KNOW_CHOICES = [
    ("", "Select One"),
    ("Facebook", "Facebook"),
    ("Instagram", "Instagram"),
    ("Linkedin", "Linkedin"),
    ("Twitter", "Twitter"),
    ("Friends", "Friends"),
    ("Friends of friends", "Friends of friends"),
    ("Family", "Family"),
    ("Others", "Others"),
]

SUBSCRIBE_CHOICES = [
    ("Yes", "Yes"),
    ("No", "No"),
    ("Maybe", "Maybe"),
]

POST_CHOICES = (
    (1, 'Story Writer (Write a story from the interview)'),
    (2, 'Interviewer (Take interview of our guests)'),
    (3, 'Graphics Designer (Design Social Media Content and Edit Photos and Videos)'),
    (4, 'Social Media Officer (Handle and Prepare Content for Social Media Platforms of VS)'),
)

class SubmitStoryModelJoinForm(forms.ModelForm):

    PRONOUNS_CHOICE = [
        ("", "Select One"),
        ("he, him, his", "he, him, his"),
        ("she, her, hers", "she, her, hers"),
        ("they, them, theirs", "they, them, theirs"),
        ("Other", "Other"),
    ]
    SECTOR_CHOICES = [
        ("", "Select One"),
        ("Education", "Education"),
        ("Animal Welfare", "Animal Welfare"),
        ("Transgender Rights", "Transgender Rights"),
        ("Women Empowerment", "Women Empowerment"),
        ("Menstrual Hygiene Works", "Menstrual Hygiene Works"),
        ("Anti-child Labor and Marriage Works", "Anti-child Labor and Marriage Works"),
        (
            "Working for Mentally and Physically Challenged",
            "Working for Mentally and Physically Challenged",
        ),
        ("Other", "Other"),
    ]
    MODE_OF_COMMUNICAION_CHOICES = [
        ("", "Select One"),
        ("Whatsapp", "Whatsapp"),
        ("Email", "Email"),
        ("Facebook Messenger", "Facebook Messenger"),
        ("Phone", "Phone"),
    ]

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    pronouns = forms.CharField(widget=forms.Select(choices=PRONOUNS_CHOICE))
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )
    sector = forms.CharField(widget=forms.Select(choices=SECTOR_CHOICES))
    mode_of_communication = forms.CharField(
        widget=forms.Select(choices=MODE_OF_COMMUNICAION_CHOICES)
    )
    story_content = forms.CharField(
        widget=TinyMCE(attrs={"cols": 80, "rows": 15, "class": "form-control"})
    )

    class Meta:
        model = SubmitStoryModel
        fields = "__all__"
        exclude = ["created_at", "updated_at"]


class VolunteerJoinModelForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP_CHOICES))
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )
    got_to_know_us = forms.CharField(widget=forms.Select(choices=GOT_TO_KNOW_CHOICES))
    subscribe_to_newsletter = forms.CharField(widget=forms.Select(choices=SUBSCRIBE_CHOICES))


    class Meta:
        model = VolunteerJoinModel
        fields = "__all__"
        exclude = ["created_at", "updated_at"]