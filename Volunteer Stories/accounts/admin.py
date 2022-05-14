from django.contrib import admin
from django.utils.html import format_html
from accounts.models import Image, Volunteer


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


class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "gender",
        "country",
        "assigned_to",
        "created_at",
    )
    search_fields = (
        "assigned_to",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    filter_horizontal = ()
    ordering = ("-created_at",)
    fieldsets = ()
    list_filter = (
        "assigned_to",
    )


admin.site.register(Image, ImageAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
