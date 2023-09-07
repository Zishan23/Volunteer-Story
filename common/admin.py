from django.contrib import admin

from common.models import BaseModel


class RawIdFieldsAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(RawIdFieldsAdmin, self).__init__(*args, **kwargs)
        # make all ForeignKey fields use raw_id_fields
        self.raw_id_fields = [field.name for field in self.model._meta.get_fields() if
                              field.is_relation and field.many_to_one]
        if issubclass(self.model, BaseModel):
            timestamp_fields = [
                'created_at',
                'updated_at',
            ]
            status_fields = [
                'is_active',
                'is_deleted',
            ]
            self.list_display = list(self.list_display) + timestamp_fields + status_fields
            self.readonly_fields = list(self.readonly_fields) + timestamp_fields
            self.list_filter = list(self.list_filter) + timestamp_fields + status_fields
