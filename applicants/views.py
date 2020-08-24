from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from users.models import User
from contacts.forms import AddressForm, TelephoneForm, EmailForm
from contacts.models import Address, Telephone, Email
from .forms import ApplicantCreationForm
from .models import Applicant


class ApplicantCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Applicant
    template_name = 'applicants/create_applicant.html'
    fields = ['prefix', 'first_name', 'last_name', 'suffix']

    def form_valid(self, form):
        """ Add the logged-in user to the object's 'created_by' field. """
        applicant = self.object
        applicant = form.save(commit=False)
        applicant.created_by = self.request.user
        applicant.save()
        return super().form_valid(form)

        
class ApplicantListView(LoginRequiredMixin, ListView):
    model = Applicant
    template_name = 'applicant/applicant_list.html'
    context_object_name = 'applicants'
    ordering = ['last_name']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Applicant.objects.all()
        return Applicant.objects.filter(created_by=self.request.user)

class ApplicantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    # for template context, use 'applicant' or 'object'
    model = Applicant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = Address.objects.all()
        context['telephone'] = Telephone.objects.all()
        context['email'] = Email.objects.all()
        return context

    def test_func(self):
        self.applicant = self.get_object()
        if self.request.user.is_staff or self.request.user == self.applicant.created_by:
            return True
        return False

class ApplicantUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Applicant
    fields = ['prefix', 'first_name', 'last_name', 'suffix']
    template_name = 'applicants/applicant_update.html'
    success_message = 'Contact detail has been updated successfully!'

    def test_func(self):
        self.applicant = self.get_object()
        if self.request.user.is_staff or self.request.user == self.applicant.created_by:
            return True
        return False

class ApplicantNoteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Applicant
    fields = ['notes']
    template_name = 'applicants/applicant_update.html'
    success_message = 'Contact detail has been updated successfully!'

    def test_func(self):
        self.applicant = self.get_object()
        if self.request.user.is_staff or self.request.user == self.applicant.created_by:
            return True
        return False