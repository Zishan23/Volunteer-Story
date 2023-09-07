from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from blog.models import Category, SubCategory, Comment, Newsletter, Post

from common.admin import RawIdFieldsAdmin


@admin.register(Newsletter)
class NewsletterAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'id',
        'email',
    )
    list_display_links = ('id', 'email')
    list_filter = ('email',)
    search_fields = ('email',)
    # fieldsets = (
    #     (None, {'fields': ('name', 'email', 'address', 'city',
    #      'state', 'zip', 'service_type', 'extra_services')}),
    #     ('Status', {'fields': ('is_active', 'is_deleted', 'is_answered')}),
    #     ('Dates', {'fields': ('created_at', 'updated_at')}),
    # )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", ]
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
    list_display = ["name", "email", "content", "post", "created_at"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    list_per_page = 25


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "sub_category", "created_at"]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]
    list_per_page = 25


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
