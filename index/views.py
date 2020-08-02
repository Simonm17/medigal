from django.shortcuts import render
from django.utils import timezone
import datetime
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    return render(request, 'index/home.html', context={
        'title': 'Worker\'s Compensation Online QME/AME Scheduler',
        'timezone': timezone.now(),  # only using if wanting to display UTC timezone.
        'datetime': datetime.datetime.now()  # displays current local timezone
    })

class Get404View(TemplateView):
    template_name = 'index/404error.html'