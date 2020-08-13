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

class AppointmentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Appointment
    fields = '__all__'
    template_name = 'scheduling/appointment_view.html'

    def test_func(self):
        self.appointment = self.get_object()
        if self.request.user.is_staff:
            return True
        return False
