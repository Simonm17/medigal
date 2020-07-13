from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been successfully created! You may now log in.')
            return redirect('index-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', context={'form': form, 'title': 'Register'})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index-home')
        else:
            messages.warning(request, 'Invalid email address or password. Please try again.')
            form = LoginForm()
    else:
        form = LoginForm()
    return render(request, 'web/home.html', context={'form': form})
