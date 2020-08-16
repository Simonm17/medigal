from django.forms import ModelForm
from django import forms

from .models import Applicant

class ApplicantCreationForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['prefix', 'first_name', 'last_name', 'suffix']
