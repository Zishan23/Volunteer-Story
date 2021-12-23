# -*- coding: utf-8 -*-
from django.contrib import admin

from blog.models import Category, Comment, Newsletter, Post

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]
    list_display_links = ["email"]
    list_filter = ["email"]
    search_fields = ["email"]
    list_per_page = 25


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter, NewsletterAdmin)
