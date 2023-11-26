from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def success_view(request):
    return render(request, 'success.html')

def logout_view(request):
    logout(request)
    return redirect('login')
