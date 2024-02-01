from django.contrib import admin

from . import models


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    list_editable = ['is_active']


class QuestionsInline(admin.TabularInline):
    model = models.Questions
    fields = ['author', 'parent', 'body']


@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['author', 'parent']

    def get_queryset(self, request):
        qs = super(QuestionsAdmin, self).get_queryset(request)
        return qs.filter(parent=None)

    inlines = [
        QuestionsInline,
    ]
