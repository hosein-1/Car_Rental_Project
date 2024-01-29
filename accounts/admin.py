from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'first_name', 'last_name', 'user_type']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'user_type', 'phone_number', 'address', 'national_code')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'user_type', 'phone_number', 'address', 'national_code')}),
    )


