from django import forms
from django.forms import ModelForm
from .models import Appointment
from django.forms.widgets import DateTimeInput

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

class AppointmentViewForm(ModelForm):

    class Meta:
        model = Appointment
        fields = ['records_sent', 'records_sent_date', 'records_received', 'records_received_date', 'notes', 'attended']

        
    # records_sent_date = forms.DateTimeField(
    #     input_formats = ['%Y-%m-%d %H:%M'],
    #     widget = forms.DateTimeInput(
    #         attrs={
    #             'type': 'datetime-local'
    #         },
    #         format='%Y-%m-%d %H:%M'
    #     ),
    # )