from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth\
from django.contrib import messages
from accounts.forms import UserSignUpForm
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser,Doctor,Patient
from django.views.generic import CreateView

def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "Patient"
            user.save()
            print('dfbghjklfhgjkl')
            patient = Patient(user=user)
            patient.save()
            # send_activation_email(user, request)
            return redirect('/')
    else:
        form = UserSignUpForm()

    context = {
        'form': form,
    }
    
    return render(request, 'sign_up.html', context)

def sign_in(request):
    
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        
        try:
            user= User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'username does not exist!') 
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in succesfully')
                return redirect('/')
            else:
                messages.error(request, 'Please activate your account')
                return redirect('/') 
        else:
                messages.error(request, 'Wrong password')
                return redirect('/') 
            
    return render(request, 'sign_up.html')
# Create your views here.
def custom_logout(request):
    logout(request)
    return redirect('accounts:sign_in')  # Assuming 'login' is the name of your login view

   