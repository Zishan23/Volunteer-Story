from django import forms
from blog.models import Comment, Newsletter


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Type your comment here...",
                "rows": 3,
            }
        )
    )

    class Meta:
        model = Comment
        fields = ("name", "email", "content",)


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email address",
                "required": True,
            }
        )
    )

    class Meta:
        model = Newsletter
        fields = ("email",)
