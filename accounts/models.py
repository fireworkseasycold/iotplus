from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class MyProfile(models.Model):
    """用户信息拓展-用户信息类"""
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=20, blank=True)
    mugshot = models.ImageField(upload_to='upload',default = 'upload/none.jpg', blank=True)   #头像
    is_developer = models.BooleanField(default=True)
    is_custom_user = models.BooleanField(default=False)

    def __str__(self):  # Python 3: def __str__(self):
        return self.user.username  


#django的信号装饰器，创建新用户时候，同时创建信息表
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = MyProfile.objects.get_or_create(user=instance)