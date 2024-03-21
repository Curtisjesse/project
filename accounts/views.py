from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth\
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def register(request):
    
    if request.method == 'POST':
            
        
        fullname = request.POST['Full_name']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        
        if password1 != password2:
            return messages(request, "password didn't match")
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            # Any additional fields can be set here
            first_name=fullname.split()[0],
            last_name=fullname.split()[1] if len(fullname.split()) > 1 else ''
        )
        user.save()
        print('user created')
        return redirect('/')
    else: 
         return render(request, 'sign_up.html')

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
