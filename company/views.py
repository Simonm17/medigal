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
    success_message = 'Your request has been submitted and is pending review. You will receive an email with updates on your request.'
    success_url = '/'

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)


"""
CompanyCreateView will require a filtering of the Request object where it displays ONE object with reviewed = False
In the CCV there will also need to be some script where once company is created, the reviewed is set to True.
"""

"""
We will make a request detail view, where staff and requester have permissions to view the request pending approval/denial. Use def test_func to filter the two users.

Learn signal sending for when user is accepted.
NEED TO MODIFY REQUEST FIELD TO ADD rejected_booleanfield.

Also make update view for staff to accept or deny form.
"""