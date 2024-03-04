from django.shortcuts import render
from .models import Doctors , Departments

def index(request):
    
    return render(request, "index.html")

def blog(request):
    
    return render(request, "blog.html")

def contact(request):
    
    return render(request, "contact.html")

def departments(request):
    
    departments = Departments.objects.all().order_by('?')[:6]
    context = {
        'departments' : departments , 
        "nav" : 'departments',
         }
    
    return render(request, "departments.html", context)

def about(request):
    
    return render(request, "about.html")

def doctor(request):
    
    doctor = Doctors.objects.all().order_by('?')[:4]
    context = {
        'doctor' : doctor , 
        "nav" : 'doctor',
         }
    
    return render(request, "doctor.html", context )

def appointment(request):
    
    return render(request, "appointment.html")

def terms(request):
    
    return render(request, "terms.html")

def privacy(request):
    
    return render(request, "privacy.html")

def login(request):
    
    return render(request, "login.html")

def register(request):
    
    return render(request, "register.html", {'nav':'register'})


# Create your views here.
