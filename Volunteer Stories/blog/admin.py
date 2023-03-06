from django.contrib import admin

from blog.models import CategoryModel, SubCategoryModel, CommentModel, NewsletterModel, PostModel


class NewsletterModelAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]
    list_display_links = ["email"]
    list_filter = ["email"]
    search_fields = ["email"]
    list_per_page = 25


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title",]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    list_per_page = 25


class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    list_per_page = 25


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "post", "timestamp"]
    list_display_links = ["user"]
    list_filter = ["user"]
    search_fields = ["user"]
    list_per_page = 25


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "sub_category", "timestamp"]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    list_per_page = 25


admin.site.register(PostModel, PostModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(SubCategoryModel, SubCategoryModelAdmin)
admin.site.register(CommentModel, CommentModelAdmin)
admin.site.register(NewsletterModel, NewsletterModelAdmin)
