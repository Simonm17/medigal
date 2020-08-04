from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
    success_message = 'Your request has been submitted and is pending review. In the meatime, you may review and make any changes.'

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)

    

class RequestDetailView(LoginRequiredMixin, DetailView):
    model = Request
    template_name = 'company/request_detail.html'

    def test_func(self):
        # verify if logged in user == requester
        # user = self.request.user
        if self.request.user.is_staff:
            return True
        else:
        # False returns 403 page (permission denied)
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'View your company register request ticket'

class RequestUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Request
    fields = [
        'company_name', 'company_address', 'company_telephone', 'company_website'
    ]
    template_name = 'company/request_update.html'
    context_object_name = 'requester'
    success_message = 'Your request has been updated!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Make changes to submitted request to register company'
        return context

    def test_func(self):
        if self.request.user.is_staff or self.request.user:
            return True
        # False returns 403 page (permission denied)
        return False

class RequestListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Request
    context_object_name = 'requests'
    template_name = 'company/request_list.html'
    ordering = ['request_date']
    paginate_by = 100

    def test_func(self):
        if self.request.user.is_staff:
            return True
        # False returns 403 page (permission denied)
        return False


#NOTE: not routed
class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
    template_name = 'company/create_company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Need to be able to get id of Request object from previously clicked Request object from ListView
        context['request_id'] = self.request.GET.get('requestid')
        context['request'] = Request.objects.get(id=context['request_id'])
        return context

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