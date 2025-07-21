from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

from django.contrib.auth.models import User
from django.db import IntegrityError


from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except IntegrityError:
                form.add_error('username', 'Username already exists. Please choose another one.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})




def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error = "Invalid username or password"
    return render(request, 'accounts/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')
