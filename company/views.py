from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Company, Request
from users.models import User
class RequestCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Request
    fields = [
        'company_name', 'company_address', 'company_telephone', 'company_website'
    ]
    template_name = 'company/request.html'
    success_message = 'Your request has been submitted. Please refer to your email for further instructions and updates.'
    success_url = '/'

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)


"""
CompanyCreateView will require a filtering of the Request object where it displays ONE object with reviewed = False
In the CCV there will also need to be some script where once company is created, the reviewed is set to True.
"""