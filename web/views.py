from django.shortcuts import render

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
    
    return render(request, "doctor.html")

def appointment(request):
    
    return render(request, "appointment.html")


# Create your views here.
