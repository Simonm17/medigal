from django.shortcuts import render
from .models import Appointment
from .forms import NewAppointmentForm
from applicants.models import Applicant
from doctors.models import Doctor
from contacts.models import Address, Telephone, Email
from users.models import User

from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404



class NewAppointmentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Appointment
    # fields = ['appointment_type', 'applicant', 'doctor', 'appointment_date', 'panel_number']
    template_name = 'scheduling/new_appointment.html'
    success_message = 'Appointment has been created successfully!'
    form_class = NewAppointmentForm

    def get_form(self, *args, **kwargs):
        #Using get_form because CreateView doesn't have get_queryset
        form = super().get_form(*args, **kwargs)
        form.fields['applicant'].queryset = Applicant.objects.filter(created_by=self.request.user)
        return form

