from django import forms

from django.forms import ModelForm, Textarea, TextInput
from .models import Company, Request

"""
PLAN:
    Users will be given a form to request a company creation. 
    form fields = modelForm of company
    Once form is submitted, it will be sent to django staff for review and manual creation.
    Once created, submitting user will be given an email notifying of the creation/rejection of the company.

    Users will need to show company website domain or some other proof.

    Staff will have access to createview which has test_func/userpassesmixin that returns django staff. don't mistaken with company staff.

    Once company is created, user will be made staff.

"""

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            'company_name', 'company_address', 'company_telephone', 'company_website'
        ]


class CompanyCreationForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'party_type']