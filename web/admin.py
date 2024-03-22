from django.contrib import admin

from .models import Doctors,Departments,Blog,Medicine,Testimonials,Booking_Detail,Contact_info
# Register your models here.
admin.site.register(Doctors)
# admin.site.register(Socialmedia)
admin.site.register(Departments)
admin.site.register(Blog)
admin.site.register(Medicine)
admin.site.register(Testimonials)
admin.site.register(Contact_info)
admin.site.register(Booking_Detail)
