from django.urls import path, include
from rest_framework import routers
from flutterapp import views

router = routers.DefaultRouter()
router.register(r'compvision', views.CompVisionFViewSet)

urlpatterns = [
    path('', include(router.urls))
]
