from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city', )
    list_display_links = ('name', )
    search_fields = ('name', )
    ordering = ('-id', )
