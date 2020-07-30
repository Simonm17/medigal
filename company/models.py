from django.db import models
from contacts.models import Address, Telephone, Email


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
