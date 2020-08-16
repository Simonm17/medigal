from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from contacts.models import Address, Telephone, Email
from contacts.forms import AddressForm, TelephoneForm, EmailForm
from .models import Company, Request
from .forms import CompanyCreationForm


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


class RequestUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
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
        self.requesting_user = self.get_object()
        if self.request.user.is_staff or self.request.user == self.requesting_user.requester:
            return True
        # False returns 403 page (permission denied)
        return False

class RequestDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Request

    def test_func(self):
        """ Checks if current user is site staff or Request user. 
        If true, grant permission. If false, return 403 error. """
        self.requesting_user = self.get_object()
        if self.request.user.is_staff or self.request.user == self.requesting_user.requester:
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
        return False


class CompanyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Company
    fields = ['name', 'party_type']
    template_name = 'company/create_company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Need to be able to get id of Request object from previously clicked Request object from ListView
        context['request_id'] = self.request.GET.get('requestid')
        context['request'] = Request.objects.get(id=context['request_id'])
        context['address_form'] = AddressForm()
        context['telephone_form'] = TelephoneForm()

        return context

    # def form_valid(self, form, a_form, t_form, e_form):


    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

def user_check(user):
    return user.is_staff

# Todo: need to make a denied function
@user_passes_test(user_check)
def create_company(request):
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST)
        a_form = AddressForm(request.POST)
        t_form = TelephoneForm(request.POST)
        e_form = EmailForm(request.POST)
        request_id = request.GET.get('requestid')
        if form.is_valid() and a_form.is_valid() and t_form.is_valid() and e_form.is_valid():
            form.save()
            a_form.save()
            t_form.save()
            e_form.save()

            company = Company.objects.last()
            company.address.add(Address.objects.last())
            company.telephone.add(Telephone.objects.last())
            company.email.add(Email.objects.last())
            company.save()
            messages.success(request, f'Company has been successfully created.')

            # Once company is accepted and created, check off request ticket.
            requested_object = Request.objects.get(id=request_id)
            requested_object.reviewed = True
            requested_object.accepted = True
            requested_object.save()

            # Add company to user model's company field
            get_email = requested_object.requester # get requester's email
            get_user = User.objects.get(email=get_email) # get user from User's model
            get_user.company = company # add the newly created company to user's company field
            get_user.is_company_admin = True # Give user admin status
            get_user.save()

            return redirect('request_list')
    else:
        form = CompanyCreationForm()
        a_form = AddressForm()
        t_form = TelephoneForm()
        e_form = EmailForm()
        request_id = request.GET.get('requestid')
        requested_object = Request.objects.get(id=request_id)
    return render(request, 'company/create_company.html', context={
        'form': form,
        'a_form': a_form,
        't_form': t_form,
        'e_form': e_form,
        'request': Request.objects.get(id=request_id),
        'title': 'Create new company',
    })

"""
CompanyCreateView will require a filtering of the Request object where it displays ONE object with reviewed = False
In the CCV there will also need to be some script where once company is created, the reviewed is set to True.
"""

"""
Learn signal sending for when user is accepted.
NEED TO MODIFY REQUEST FIELD TO ADD rejected_booleanfield.

Also make update view for staff to accept or deny form.
"""