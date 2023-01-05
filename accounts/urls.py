from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'myprofile', views.MyProfileViewSet, basename='myprofile')

urlpatterns = [
    url(r'^', include(router.urls)),
]