from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateTimeInput

from .models import Appointment


class NewAppointmentForm(ModelForm):
    appointment_date = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'
            },
            format='%Y-%m-%dT%H:%M'
        )
    )

    class Meta:
        model = Appointment
        fields = ['appointment_type', 'exam_type', 'applicant', 'doctor', 'appointment_date', 'panel_number']
        # widgets = {
        #     'appointment_date': DateTimeInput(attrs={
        #         'type': 'datetime-local'
        #     }),
        # }
        