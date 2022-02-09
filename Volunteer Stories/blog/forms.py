# -*- coding: utf-8 -*-
from django import forms
from tinymce.widgets import TinyMCE

from blog.models import Comment, Post


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={"cols": 80, "rows": 15, "class": "form-control"})
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "overview",
            "content",
            "featured",
            "category",
            "sub_category",
            "thumbnail",
        )


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
        fields = ("content",)
