from django.forms import ModelForm
from django import forms
from .models import Doctor, Address, Telephone, Email

class DoctorCreationForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name']
    
class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone
        fields = '__all__'

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'