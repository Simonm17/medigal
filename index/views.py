import datetime

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.base import TemplateView

from company.models import Request
from users.models import User


# Create your views here.
def home(request):
    context = {
        'title': 'Worker\'s Compensation Online QME/AME Scheduler',
        'timezone': timezone.now(),  # only using if wanting to display UTC timezone.
        'datetime': datetime.datetime.now(),  # displays current local timezone
        'user': request.user,
    }

    if request.user.is_authenticated:
        try:
            requester = Request.objects.get(requester=request.user)
            context['requester'] = requester
        except Request.DoesNotExist:
            pass
    return render(request, 'index/home.html', context)



class Get404View(TemplateView):
    template_name = 'index/404.html'