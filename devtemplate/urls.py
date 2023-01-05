from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
#from rest_framework_nested import routers
from .views import DevTemplateViewSet

router = routers.DefaultRouter()  #DefaultRouter会比SimpleRouter多附带一个默认的API根视图
#router = routers.SimpleRouter()
router.register(r'devtemplates', DevTemplateViewSet,basename='devtemplates')

urlpatterns = [
    url(r'^', include(router.urls)),
]