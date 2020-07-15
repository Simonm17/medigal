from django.shortcuts import render
from django.utils import timezone
import datetime


# Create your views here.
def home(request):
    return render(request, 'index/home.html', context={
        'timezone': timezone.now(),  # only using if wanting to display UTC timezone
        'datetime': datetime.datetime.now()  # displays current local timezone
    })