from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import (
    Category,
    Movie,
)


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ['title', 'created', 'modified']
    list_filter = ['created']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie)
