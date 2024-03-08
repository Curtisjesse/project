from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Doctors , Departments , Blog , Medicine, Testimonials

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

def contact(request):
    
    return render(request, "contact.html")

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
    return render(request, "appointment.html")

@login_required
def terms(request):
    
    return render(request, "terms.html")

@login_required
def privacy(request):
    
    return render(request, "privacy.html")

def login(request):
    
    return render(request, "login.html")
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
