from django.contrib import admin

from .models import (
    Category,
    Idea,
)


admin.site.register(Category)
admin.site.register(Idea)
