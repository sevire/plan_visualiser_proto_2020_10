from django.db import models
from django.conf import settings
from django.db.models import UniqueConstraint


class FileType(models.Model):
    file_type_name = models.CharField(max_length=50)
    file_type_description = models.CharField(max_length=100)

    def __str__(self):
        return self.file_type_name


class Plan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Upload files into folder under MEDIA_ROOT
    original_file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to="plan_files", null=True)
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)

    class META:
        constraints = UniqueConstraint(fields=['user', 'original_file_name'], name="unique_filename_for_user")

    def __str__(self):
        return f'{self.file}:{self.file_type}'
