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
        return f'{self.original_file_name}:{self.file_type}'


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    red = models.IntegerField(null=False, default=0)
    green = models.IntegerField(null=False, default=0)
    blue = models.IntegerField(null=False, default=0)
    alpha = models.FloatField(null=False, default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(red__gte=0) & models.Q(red__lte=255),
                name="Red component must be between 0 and 255 (inclusive)",
            ),
            models.CheckConstraint(
                check=models.Q(green__gte=0) & models.Q(green__lte=255),
                name="Green component must be between 0 and 255 (inclusive)",
            ),
            models.CheckConstraint(
                check=models.Q(blue__gte=0) & models.Q(blue__lte=255),
                name="Blue component must be between 0 and 255 (inclusive)",
            ),
            models.CheckConstraint(
                check=models.Q(alpha__gte=0) & models.Q(alpha__lte=1),
                name="Alpha value must be between 0 and 1",
            ),
        ]

    def __str__(self):
        return f"([{self.name}]-{self.red},{self.green},{self.blue},{self.alpha})"


class Font(models.Model):
    font_name = models.CharField(max_length=100)

    def __str__(self):
        return self.font_name


class PlotableStyle(models.Model):
    style_name = models.CharField(max_length=100)
    fill_color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name="plotablestyle_fill")
    line_color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name="plotablestyle_line")
    line_thickness = models.IntegerField()
    font = models.ForeignKey(Font, on_delete=models.PROTECT)


class PlanVisual(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100)
    width = models.FloatField(default=30)
    max_height = models.FloatField(default=20)
    include_title = models.BooleanField(default=True)