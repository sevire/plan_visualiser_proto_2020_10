from django.urls import path
from plan_visualiser_django import views
from plan_visualiser_django.views import delete_plan

urlpatterns = [
    path("add-plan", views.add_plan),
    path("add-visual/<int:plan_id>", views.add_visual),
    path("edit-visual/<int:visual_id>", views.edit_visual),
    path("manage-plans", views.manage_plans, name="manage_plans"),
    path("delete-plan/<int:pk>/", views.delete_plan, name='delete_plan'),
    path("delete-visual/<int:pk>/", views.delete_visual, name='delete_visual'),
    path("manage-visuals/<int:plan_id>/", views.manage_visuals, name='manage_visuals')
]
