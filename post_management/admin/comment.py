from django.contrib import admin
from simple_history_field_track.admin import SimpleAdminDiffHistory

from post_management.models import Comment


@admin.register(Comment)
class CommentAdmin(SimpleAdminDiffHistory):
    list_display = ('pk', 'post', 'context', 'owner', 'created', 'modified')
    search_fields = ('pk', 'post', 'owner' 'context')
    readonly_fields = ('pk',)
    filter_horizontal = ()
    list_filter = ('owner', )
    fieldsets = (
        ('Tweet info', {
            'fields': ('post',)
        }),
        ('comment info', {
            'fields': ('pk', ('context', 'owner'))
        }),
    )
