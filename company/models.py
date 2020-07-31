from django.db import models
from contacts.models import Address, Telephone, Email
import users.models

class Company(models.Model):
    APPLICANT = 'APP'
    DEFENSE = 'DEF'
    PARTY_TYPE = [
        (APPLICANT, 'Applicant'),
        (DEFENSE, 'Defense')
    ]
    name = models.CharField(unique=True, max_length=250)
    address = models.ManyToManyField(Address)
    telephone = models.ManyToManyField(Telephone)
    email = models.ManyToManyField(Email)
    party_type = models.CharField(max_length=10, choices=PARTY_TYPE)
    
    def __str__(self):
        return self.name

class Request(models.Model):
    # user submission fields
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=250) # doesn't need unique=True becaue Company model field already has unique validation
    company_address = models.TextField()
    company_telephone = models.IntegerField()
    company_website = models.CharField(max_length=120, blank=True)

    # staff validation fields
    notes = models.TextField(blank=True)
    reviewed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Request ticket #{self.id}'
