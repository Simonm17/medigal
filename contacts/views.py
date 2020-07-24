from django.shortcuts import render, redirect
from users.models import User
from .models import Address, Telephone, Email
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    fields = '__all__'
    template_name = 'contacts/address_update.html' 