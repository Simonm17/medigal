from django.db import models
from django.urls import reverse

from contacts.models import Person

# Create your models here.
class Applicant(Person):

    # For UpdateView to reverse back to after form POST request
    def get_absolute_url(self):
        return reverse('applicant_detail', kwargs={'pk': self.pk})
