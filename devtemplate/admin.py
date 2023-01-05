from django.contrib import admin
from .models import DevTemplate

# class DevTemplateAdmin(admin.ModelAdmin):
#     fields = ['title', 'description','img','device_type','is_custom_registered','protocal_type','owner']
#     list_display = ['id','title', 'description','img','device_type','is_custom_registered','protocal_type','owner','updated','created']

# admin.site.register(DevTemplate,DevTemplateAdmin)
admin.site.register(DevTemplate)