django_drf的物联网后台管理系统

devtemplate是demo不用管
device 设备
iothub 订阅


##环境安装，多个第三方库和代码存在版本冲突不匹配的问题，解决中
-i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django==3.2.14 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install mongoengine -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install djangorestframework -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install drf_yasg -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install djangorestframework-simplejwt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django-allauth -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django-rest-auth -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install drf-nested-routers -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paho.mqtt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
###先创建用户并登录，否则queryset = DevTemplate.objects.filter(owner=request.user).order_by('-created')测试时候报错
python manage.py createsuperuser

oldenv版本“”“
pip install django==3.2 i https://pypi.douban.com/simple/
pip install djangorestframework==3.9.0 -i https://pypi.douban.com/simple/
pip install drf-yasg==1.11.3 -i https://pypi.douban.com/simple/
pip install django-rest-auth==0.9.3 django-rest-swagger==2.1.2 djangorestframework==3.9.0 djangorestframework-simplejwt==4.0.0 -i https://pypi.douban.com/simple/
”“”
swagger界面点击tokenapi的post,输入账户密码获取access
右上角authorize输入Bearer加上获取的access

认证jwtoken或者rest-auth二选一,在swagger界面，这两个第三方库的配置认证有冲突





如果：  File "D:\物联网\浆果物联网\iotplus\venv\lib\site-packages\django\contrib\auth\models.py", line 420, in __int__
    raise TypeError('Cannot cast AnonymousUser to int. Are you trying to use it in place of User?')
TypeError: Cannot cast AnonymousUser to int. Are you trying to use it in place of User?
必须专门添加id字段，而不是total user对象

\iotplus\venv\lib\site-packages\rest_framework\views.py", line 278, in get_permissions
    return [permission() for permission in self.permission_classes]
TypeError: 'BasePermissionMetaclass' object is not iterable'
原因：是settings文件中的rest_framework在冒号后加中括号


