from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from users.models import User
from .models import Address, Telephone, Email
from doctors.models import Doctor
from applicants.models import Applicant
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin



class AddressDetailView(DetailView):
    model = Address

class AddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Address
    fields = '__all__'
    template_name = 'contacts/address_update.html' 
    success_message = 'Address has been updated successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = Doctor.objects.all()
        context['applicant'] = Applicant.objects.all()
        context['next_url'] = self.request.GET.get('next') # pass `next` parameter received from previous page to the context
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url


class TelephoneDetailView(DetailView):
    model = Telephone

class TelephoneUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Telephone
    fields = '__all__'
    template_name = 'contacts/telephone_update.html'
    success_message = 'Telephone number has been updated successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = Doctor.objects.all()
        context['applicant'] = Applicant.objects.all()
        context['next_url'] = self.request.GET.get('next') # pass `next` parameter received from previous page to the context
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url

class EmailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Email
    fields = '__all__'
    template_name = 'contacts/email_update.html'
    success_message = 'Email has been updated successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = Doctor.objects.all()
        context['applicant'] = Applicant.objects.all()
        context['next_url'] = self.request.GET.get('next') # pass `next` parameter received from previous page to the context
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        
class TelephoneUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Telephone
    fields = '__all__'
    template_name = 'contacts/telephone_update.html'
    success_message = 'Telephone has been updated successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = Doctor.objects.all()
        context['applicant'] = Applicant.objects.all()
        context['next_url'] = self.request.GET.get('next') # pass `next` parameter received from previous page to the context
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url