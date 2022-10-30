from django.contrib import admin
from plan_visualiser_django.models import FileType, Plan


@admin.register(FileType)
class FileTypeAdmin(admin.ModelAdmin):
    list_display = ["file_type_name", "file_type_description"]


@admin.register(Plan)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ["user", "file", "file_type"]