from django.forms import ModelForm
from plan_visualiser_django.models import Plan


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ("file", "file_type")