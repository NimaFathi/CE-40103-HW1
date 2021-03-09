from django.contrib import admin
from simple_history_field_track.admin import SimpleAdminDiffHistory

from post_management.models import Tweet


@admin.register(Tweet)
class TweetAdAdmin(SimpleAdminDiffHistory):
    list_display = ('pk', 'owner', 'context', 'created', 'modified')
    search_fields = ('pk', 'owner__username', 'context')
    readonly_fields = ('pk',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
