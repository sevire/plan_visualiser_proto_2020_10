from django.forms import ModelForm
from plan_visualiser_django.models import Plan, PlanVisual


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ("file", "file_type")


class VisualFormForAdd(ModelForm):
    class Meta:
        model = PlanVisual
        fields = ("name",)


class VisualFormForEdit(ModelForm):
    class Meta:
        model = PlanVisual
        fields = ("name", "width", "max_height","include_title","max_height")
