from django.contrib import admin

from . import models


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    list_editable = ['is_active']
