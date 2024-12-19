from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewset

router = DefaultRouter()
router.register('users',UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]