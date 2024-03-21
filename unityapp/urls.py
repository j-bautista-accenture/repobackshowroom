from django.urls import path, include
from rest_framework import routers
from unityapp import views

router = routers.DefaultRouter()
router.register(r'compvision', views.CompVisionUViewSet)

urlpatterns = [
    path('', include(router.urls))
]
