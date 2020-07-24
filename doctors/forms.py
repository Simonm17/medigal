from django.forms import ModelForm
from .models import Doctor

class DoctorCreationForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name']