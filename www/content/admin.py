from django.contrib import admin
from django.contrib.admin.models import LogEntry
from . import models


@admin.register(models.Communication)
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = [
        'name',
        'email',
        'date_created',
        'phone_number']
    readonly_fields = ['request_meta']


@admin.register(models.Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['name', 'upload_file', 'date_created']
    readonly_fields = ['date_created']


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'action_time', 'user', 'object_repr', 'content_type', 'change_message'
    ]
    list_filter = ['user']
    readonly_fields = [
        'content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
