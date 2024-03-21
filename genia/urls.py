from django.urls import path, include
from rest_framework import routers
from genia import views

router = routers.DefaultRouter()
router.register(r'rag', views.GenIAViewSet)

urlpatterns = [
    path('', include(router.urls))
]
