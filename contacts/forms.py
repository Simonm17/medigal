from django.forms import ModelForm
from django import forms
from .models import Doctor, Address, Telephone, Email

class DoctorCreationForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=120)
    last_name = forms.CharField(label="Last Name", max_length=120)
    
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