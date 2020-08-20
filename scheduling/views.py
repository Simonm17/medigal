from datetime import datetime

from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.forms.widgets import DateTimeInput
from django.shortcuts import render, redirect
from django.utils import timezone

from applicants.models import Applicant
from doctors.models import Doctor
from contacts.models import Address, Telephone, Email
from users.models import User
from .models import Appointment
from .forms import NewAppointmentForm, AppointmentViewForm


class NewAppointmentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Appointment
    template_name = 'scheduling/new_appointment.html'
    success_message = 'Appointment has been created successfully!'
    form_class = NewAppointmentForm # If using form_class, can't use fields because it's declared in the ModelForm

    def get_form(self, *args, **kwargs):
        #Using get_form because CreateView doesn't have get_queryset
        form = super().get_form(*args, **kwargs)
        form.fields['applicant'].queryset = Applicant.objects.filter(created_by=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.scheduled_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Schedule a new medical-legal appointment'
        return context


class AppointmentListView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, ListView):
    model = Appointment
    context_object_name = 'appointment'

    def get_queryset(self):
        filter_users = Appointment.objects.filter(scheduled_by=self.request.user)
        filter_order = filter_users.order_by('appointment_date')
        return filter_order

    def test_func(self):
        if self.request.user.is_authenticated:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'View scheduled appointments'
        return context


class AppointmentView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Appointment
    # form_class = AppointmentViewForm
    fields = ['records_sent', 'records_received', 'notes', 'attended']
    template_name = 'scheduling/appointment_view.html'
    success_message = 'Updated successfully!'


    def test_func(self):
        self.appointment = self.get_object()
        if self.request.user.is_staff or self.request.user == self.appointment.scheduled_by:
            return True
        return False

    def form_valid(self, form):
        """ Update sent/received datetimes to current time
        when sent/received is checked from false to true.
        """
        appointment = self.object
        if form.instance.records_sent and appointment.b_records_sent != form.instance.records_sent:
            appointment.records_sent_date = timezone.now()
        if form.instance.records_received and appointment.b_records_received != form.instance.records_received:
            appointment.records_received_date = timezone.now()
        return super().form_valid(form)
