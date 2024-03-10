from django.contrib import admin
from .models import Books

@admin.register(Books)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
