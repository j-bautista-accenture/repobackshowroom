from django.urls import path
from .views import *

urlpatterns = [
    path('', CompVisionFViewSet.as_view(), name="home"),
]
