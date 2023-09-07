from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

from accounts.models import ImageModel, SubmitStoryModel, VolunteerJoinModel, TeamMemberModel

from common.admin import RawIdFieldsAdmin


@admin.register(ImageModel)
class ImageAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    def edit_button(self, obj):
        return format_html(
            '<a class="btn" href="/admin/accounts/image/{}/change/">Edit</a>', obj.id
        )

    list_display = (
        "id",
        "image",
        "is_hero",
        "is_divider",
        "is_gallery",
        # "edit_button",
    )
    search_fields = ()
    readonly_fields = (
    )

    filter_horizontal = ()
    ordering = ("-created_at",)
    fieldsets = ()


@admin.register(SubmitStoryModel)
class NewsletterAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "is_reviewed",
        "is_verified",
        "is_published",
        "reviewed_by",
        "verified_by",
        "published_by",
    )
    search_fields = (
        "reviewed_by",
        "verified_by",
        "published_by",
    )
    readonly_fields = (
    )

    filter_horizontal = ()
    ordering = ("-created_at",)
    fieldsets = ()
    list_filter = (
        "reviewed_by",
        "verified_by",
        "published_by",
    )


@admin.register(VolunteerJoinModel)
class NewsletterAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        "id",
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
    )
    filter_horizontal = ()
    ordering = ("-created_at",)
    fieldsets = ()


@admin.register(TeamMemberModel)
class TeamMemberModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'id',
        'name',
        'designation',
        'serial',
    )
    list_filter = (
    )
    search_fields = ('name', 'designation')
    fieldsets = (
        (None, {'fields': (
            'name', 'designation', 'image', 'serial', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link')}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
