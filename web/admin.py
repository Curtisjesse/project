from django.contrib import admin

from .models import Doctors,Socialmedia,Departments,Blog,Medicine,Testimonials,Contact_info
# Register your models here.
admin.site.register(Doctors)
admin.site.register(Socialmedia)
admin.site.register(Departments)
admin.site.register(Blog)
admin.site.register(Medicine)
admin.site.register(Testimonials)
admin.site.register(Contact_info)
