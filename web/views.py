from django.shortcuts import render
from .models import Doctors

def index(request):
    
    return render(request, "index.html")

def blog(request):
    
    return render(request, "blog.html")

def contact(request):
    
    return render(request, "contact.html")

def departments(request):
    
    return render(request, "departments.html")

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


# Create your views here.
