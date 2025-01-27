from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CreateUserForm
from django.contrib.messages import constants as messages

# from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def login_view(request):
    submitted = False
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        # messages.info(request, 'Username OR Password is incorrect!')
    return render(request, 'login.html', {'form': form})

def register_view(request):
    submitted = False
    # form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('username')
            # messages.success(request, 'Account created for ' + user)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})

# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')