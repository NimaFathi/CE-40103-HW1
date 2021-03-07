from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account_management.models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('pk', 'username', 'created', 'modified', 'is_admin', 'is_active')
    search_fields = ('pk', 'username')
    readonly_fields = ('pk', 'created', 'last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
