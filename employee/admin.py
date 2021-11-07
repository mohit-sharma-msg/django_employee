from django.contrib import admin
from .models import Employee


class AdminEmployee(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Employee)