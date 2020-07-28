from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from users.models import User
from .models import Address, Telephone, Email
from doctors.models import Doctor
from applicants.models import Applicant
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class AddressCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Address
    fields = '__all__'
    template_name = 'contacts/address_create.html'
    success_message = 'Address has been created successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_url'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            split_url = next_url.split('/')
            get_url_model = split_url[1]
            get_url_id = int(split_url[2])
            if get_url_model == 'doctors':
                doctor = Doctor.objects.get(id=get_url_id)
                doctor.address.add(Address.objects.get(id=self.object.id))
                doctor.save()
            elif get_url_model == 'applicants':
                applicant = Applicant.objects.get(id=get_url_id)
                applicant.address.add(Address.objects.get(id=self.object.id))
                applicant.save()
            return next_url

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


class TelephoneCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Telephone
    fields = '__all__'
    template_name = 'contacts/telephone_create.html'
    success_message = 'Telephone has been created successfully!'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_url'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            split_url = next_url.split('/')
            get_url_model = split_url[1]
            get_url_id = int(split_url[2])
            if get_url_model == 'doctors':
                doctor = Doctor.objects.get(id=get_url_id)
                doctor.telephone.add(Telephone.objects.get(id=self.object.id))
                doctor.save()
            elif get_url_model == 'applicants':
                applicant = Applicant.objects.get(id=get_url_id)
                applicant.telephone.add(Telephone.objects.get(id=self.object.id))
                applicant.save()
            return next_url

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


class EmailCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Email
    fields = '__all__'
    template_name = 'contacts/email_create.html'
    success_message = 'Email has been created successfully!'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_url'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            split_url = next_url.split('/')
            get_url_model = split_url[1]
            get_url_id = int(split_url[2])
            if get_url_model == 'doctors':
                doctor = Doctor.objects.get(id=get_url_id)
                doctor.email.add(Email.objects.get(id=self.object.id))
                doctor.save()
            elif get_url_model == 'applicants':
                applicant = Applicant.objects.get(id=get_url_id)
                applicant.email.add(Email.objects.get(id=self.object.id))
                applicant.save()
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