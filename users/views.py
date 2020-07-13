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
            return redirect('web-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', context={'form': form, 'title': 'Register'})