from django import forms
from django.forms import ModelForm
from .models import Doctor

class DoctorCreationForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['prefix', 'first_name', 'last_name', 'suffix']

class DoctorForm(forms.Form):
    
    PREFIX = [
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.', 'Ms.'),
        ('Miss', 'Miss'),
        ('Dr.', 'Dr.'),
        ('Hon.', 'Hon.'),
    ]

    SUFFIX = [
        ('Jr.', 'Jr.'),
        ('Sr.', 'Sr.'),
        ('Esq.', 'Esq.'),
        ('J.D.', 'J.D.'),
        ('M.D.', 'M.D.'),
        ('Ph.D.', 'Ph.D.'),
        ('Psy.D.', 'Psy.D.'),
        ('D.D.S.', 'D.D.S.'),
        ('D.P.M.', 'D.P.M.'),
        ('D.O.', 'D.O.'),
        ('D.M.D.', 'D.M.D.'),
        ('N.P.', 'N.P.'),
        ('O.D.', 'O.D.'),
        ('P.A.', 'P.A.'),
    ]

    prefix = forms.ChoiceField(choices=PREFIX, required=False)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    suffix = forms.ChoiceField(choices=SUFFIX)
    
    # Address
    ADDRESS_TYPE = [
        ('Physical', 'Physical'),
        ('Mailing', 'Mailing'),
    ]

    UNIT_TYPE = [
        ('APT', 'Apartment'),
        ('STE', 'Suite'),
        ('BLDG', 'Building'),
        ('RM', 'Room'),
        ('SPC', 'Space'),
        ('UNIT', 'Unit'),
        ('FL', 'Floor'),
    ]

    address_type = forms.ChoiceField(choices=ADDRESS_TYPE)
    address1 = forms.CharField(max_length=250)
    address2 = forms.ChoiceField(choices=UNIT_TYPE, required=False)
    city = forms.CharField(max_length=120)
    state = forms.CharField(max_length=2)
    zipcode = forms.IntegerField(min_value=5, max_value=9)

    # Telephone fields
    TELEPHONE_TYPE = [
        ('Main', 'Main'),        
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Cell', 'Cell'),
        ('Fax', 'Fax'),
        ('Other', 'Other'),
    ]
    telephone_type = forms.ChoiceField(choices=TELEPHONE_TYPE)
    telephone_number = forms.IntegerField()
    telephone_extension = forms.IntegerField(required=False)

    # Email fields
    email = forms.EmailField(max_length=250, required=False)

    # Doctor's preferences field
    by_mail = forms.BooleanField(required=False)
    by_cd = forms.BooleanField(required=False)
    by_usb = forms.BooleanField(required=False)
    by_email = forms.BooleanField(required=False)