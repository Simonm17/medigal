from django import forms
from django.forms import ModelForm

from .models import Doctor

class DoctorCreationForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['prefix', 'first_name', 'last_name', 'suffix', 'specialty']
