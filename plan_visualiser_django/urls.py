from django.urls import path
from plan_visualiser_django import views
from plan_visualiser_django.views import delete_plan

urlpatterns = [
    path("add-plan", views.add_plan),
    path("manage-plans", views.manage_plans, name="manage_plans"),
    path("delete-plan/<int:pk>/", views.delete_plan, name='delete_plan')
]
