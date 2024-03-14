from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Doctors , Departments , Blog , Medicine, Testimonials,Contact_info

def index(request):
    
    testimonials = Testimonials.objects.all()
    context = {
        
        'testimonials': testimonials }
    
    return render(request, "index.html", context)

@login_required
def blog(request):
    
    blog = Blog.objects.all().order_by('?')[:3]
    context = {
        'blog' : blog , 
        "nav" : 'blog',
         }
     
    return render(request, "blog.html",context)

def contact_info(request):
    contact_info = Contact_info.objects.all()
    context = {
        'contact_info' : contact_info,
        'nav':'contact_info',
        }
    return render(request, "contact_info.html",context)

@login_required
def departments(request):
    
    departments = Departments.objects.all().order_by('?')[:6]
    context = {
        'departments' : departments , 
        "nav" : 'departments',
         }
    
    return render(request, "departments.html", context)

@login_required
def about(request):
    
    return render(request, "about.html")

@login_required
def doctor(request):
    
    doctor = Doctors.objects.all().order_by('?')[:4]
    context = {
        'doctor' : doctor , 
        "nav" : 'doctor',
         }
    
    return render(request, "doctor.html", context ) 

@login_required
def appointment(request):
    user_name = request.user.username
    doctors = Doctors.objects.all() 
    return render(request, "appointment.html", {"doctors": doctors})

@login_required
def terms(request):
    
    return render(request, "terms.html")

@login_required
def privacy(request):
    
    return render(request, "privacy.html")

def login(request):
    
    return render(request, "login.html")

def notification(request):
    
    return render(request, "notification.html")

@login_required
def medicine(request):
    
    medicine = Medicine.objects.all().order_by('?')[:3]
    context = {
        'medicine' : medicine , 
        "nav" : 'medicine',
         }
    return render(request, "medicine.html", context)

def register(request):
    
    return render(request, "register.html", {'nav':'register'})


# Create your views here.
