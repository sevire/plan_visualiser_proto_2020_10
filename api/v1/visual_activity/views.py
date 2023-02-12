from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from api.v1.visual_activity import serializer
from plan_visualiser_django.models import VisualActivity


class VisualActivityAPI(ListCreateAPIView):
    queryset = VisualActivity.objects.all()
    serializer_class = serializer.VisualActivitySerializer
    permission_classes = (AllowAny, )