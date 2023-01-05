# Register your models here.
from django.contrib import admin
from .models import MyProfile
#配置管理员界面
admin.site.register(MyProfile)