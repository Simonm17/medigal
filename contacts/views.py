from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from users.models import User
from .models import Address, Telephone, Email
from doctors.models import Doctor
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
        return context