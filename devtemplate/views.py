
from .models import DevTemplate
from devtemplate.serializers import DevTemplateSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt import authentication


class DevTemplateViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备模板列表

    create:
    创建设备模板

    retrieve:
    查询设备模板详情

    update:
    更新设备模板

    partial_update:
    更新设备模板部分属性

    destroy:
    删除设备模板

    """

    serializer_class = DevTemplateSerializer
    # authentication_classes = (BasicAuthentication,)
    authentication_classes = (authentication.JWTAuthentication,)  #使用jwt的认证
    queryset = DevTemplate.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, ):
        # print(request.META)
        # print(request.META['HTTP_AUTHORIZATION'])
        queryset = DevTemplate.objects.filter(owner=request.user.id).order_by('-created')  # 返回登录用户创建的设备列表
        #最后解决了报错问题：原来是使用owner=request.user会出现问题swaggerui里authorize输入bearertoken的还是认证失败，改为user.id即可见https://stackoverflow.com/questions/62966136/typeerror-field-id-expected-a-number-but-got-django-contrib-auth-models-anon
        #留存疑惑：不知道为什么request.user在postman里不会出现问题，在swaggerui就会导致
        # 未解决时为了看效果用的try# 不知道原因的话就这个将就不使用token的认证访问会出错，测试用时用下方的try,except取代上一句来规避登录认证导致的错误,swaggertoken输入authorize登录认证后则不用
        # if request.user.is_authenticated:  #is_authenticated不要带（）,注意版本3以上的是属性而不是方法
        #     # 添加登录判断解决Field 'id' expected a number but got <django.contrib.auth.models.AnonymousUser object，可以尝试判断AnonymousUser，或者直接尝试获取认证的request.user.id,
        #     # https://stackoverflow.com/questions/62966136/typeerror-field-id-expected-a-number-but-got-django-contrib-auth-models-anon
        #     queryset = DevTemplate.objects.filter(owner=request.user).order_by('-created')  #返回登录用户创建的设备列表
        # else:
        #     queryset = self.queryset  #没登陆则显示所有或者提示强制登录


        # queryset = DevTemplate.objects.all()

        self.check_object_permissions(request, DevTemplate)
        serializer = DevTemplateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DevTemplate.objects.filter(owner=request.user)
        # queryset = DevTemplate.objects.all()
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request, DevTemplate)
        serializer = DevTemplateSerializer(queryset_tmp)
        return Response(serializer.data)
