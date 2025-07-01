from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def Signup(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = UserCreationForm()
    return render(request, 'Signup.html', {'form': form})

def Signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = AuthenticationForm()
    return render(request, 'Signin.html', {'form': form})

def Logout(request):
    pass