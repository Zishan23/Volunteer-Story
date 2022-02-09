from django.contrib import admin

from blog.models import Category, SubCategory, Comment, Newsletter, Post

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]
    list_display_links = ["email"]
    list_filter = ["email"]
    search_fields = ["email"]
    list_per_page = 25


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title",]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    list_per_page = 25


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    list_per_page = 25


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "post", "timestamp"]
    list_display_links = ["user"]
    list_filter = ["user"]
    search_fields = ["user"]
    list_per_page = 25


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "sub_category", "timestamp"]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    list_per_page = 25


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
