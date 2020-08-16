from django.forms import ModelForm
from django import forms

from .models import Address, Telephone, Email

    
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