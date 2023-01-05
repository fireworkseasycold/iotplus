from django.conf.urls import include, url
from rest_framework_nested import routers
from .views import IotSubDevViewSet

from django.conf import settings


#先创建一个路由实例，再注册一个url
#第一级URL
from device.urls import router
iotsubdev_router = routers.NestedSimpleRouter(router, r'devices', lookup='devices')
iotsubdev_router.register(r'iotsubdevs',IotSubDevViewSet, basename='iotsubdevs' )


urlpatterns = [
    url(r'^', include(iotsubdev_router.urls)),
]