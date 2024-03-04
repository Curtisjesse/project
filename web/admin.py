from django.contrib import admin

from .models import Doctors,Socialmedia,Departments
# Register your models here.
admin.site.register(Doctors)
admin.site.register(Socialmedia)
admin.site.register(Departments)
