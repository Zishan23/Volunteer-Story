from django.contrib import admin
from django.utils.html import format_html
from accounts.models import Image, SubmitStoryModel, VolunteerJoinModel


class ImageAdmin(admin.ModelAdmin):
    def edit_button(self, obj):
        return format_html(
            '<a class="btn" href="/admin/accounts/image/{}/change/">Edit</a>', obj.id
        )

    list_display = (
        "image",
        "is_active",
        "is_hero",
        "is_divider",
        "is_gallery",
        "edit_button",
    )
    search_fields = ()
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    filter_horizontal = ()
    ordering = ("-created_at",)
    fieldsets = ()
    list_filter = ()


class SubmitStoryModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "is_reviewed",
        "is_verified",
        "is_published",
        "reviewed_by",
        "verified_by",
        "published_by",
        "created_at",
    )
    search_fields = (
        "reviewed_by",
        "verified_by",
        "published_by",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    filter_horizontal = ()
    ordering = ("-created_at",)
    fieldsets = ()
    list_filter = (
        "reviewed_by",
        "verified_by",
        "published_by",
    )


class VolunteerJoinModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "emergency_contact"
    )
    search_fields = (
        "name",
        "email",
        "phone",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    filter_horizontal = ()
    ordering = ("-created_at",)
    fieldsets = ()


admin.site.register(Image, ImageAdmin)
admin.site.register(SubmitStoryModel, SubmitStoryModelAdmin)
admin.site.register(VolunteerJoinModel, VolunteerJoinModelAdmin)
