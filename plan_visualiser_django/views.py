import os
from tempfile import template

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from plan_visualiser_2020_10 import settings
from plan_visualiser_django.forms import PlanForm
from plan_visualiser_django.models import Plan
from django.contrib import messages


# Create your views here.

def add_plan(request):
    if request.method == "POST":
        plan_form = PlanForm(data=request.POST, files=request.FILES)
        if plan_form.is_valid():
            # Get current user
            user_model = get_user_model()
            user = user_model.objects.get(username="plan_visualiser_dev")

            # Save fields from form but don't commit so can modify other fields before comitting.
            plan = plan_form.save(commit=False)

            # Check that user hasn't already added a file with this name. Count should be zero
            count = Plan.objects.filter(user=user, original_file_name=plan.file.name).count()
            if count > 0:
                messages.error(request, f"Already uploaded a file called {plan.file.name}.  Record not added")
            else:
                # Uploaded file will be given a unique name - so need to store the name of the file the user chose.
                plan.original_file_name = plan.file.name

                # Add user to record (currently hard-coded)
                plan.user = user

                # Now can save the record
                plan.save()
                messages.success(request, "New plan saved successfully")
        else:
            messages.error(request, "Failed validation")

        return HttpResponseRedirect(reverse('manage_plans'))
    elif request.method == "GET":
        form = PlanForm()
        return render(request=request, template_name="plan_visualiser_django/pv_add_record.html", context={'form': form})
    else:
        raise Exception("Unrecognised METHOD {request['METHOD']}")


def manage_plans(request):
    # ToDo: remove hard coded user and replaced with current user.
    user_model = get_user_model()
    user = user_model.objects.get(username="plan_visualiser_dev")
    plan_files = Plan.objects.filter(user=user)

    context = {
        'user': user,
        'plan_files': plan_files
    }
    return render(request, "plan_visualiser_django/pv_manage_plans.html", context)


def delete_plan(request, pk):
    plan_record = Plan.objects.get(id=pk)

    # Before deleting record from database delete the file which was uploaded
    plan_file_path = os.path.join(settings.MEDIA_ROOT, plan_record.file.path)
    try:
        os.remove(plan_file_path)
    except OSError as e:
        messages.error(request, f"Error deleting file {plan_record.original_file_name}")

    try:
        plan_record.delete()
    except Exception:
        messages.error(request, f"Error deleting plan record for {plan_record.original_file_name}")
    else:
        messages.success(request, f"Record deleted for {plan_record.original_file_name}")

    return HttpResponseRedirect(reverse('manage_plans'))
