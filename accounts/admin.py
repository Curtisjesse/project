from django.contrib import admin

# Register your models here.
from .models import Socialmedia,Doctor,Patient,Administrator,CustomUser

admin.site.register(Socialmedia)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Administrator)
admin.site.register(CustomUser)