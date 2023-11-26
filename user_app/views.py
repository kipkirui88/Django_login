from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

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
