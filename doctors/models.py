from django.db import models
from django.urls import reverse
from contacts.models import Person

class Doctor(Person):

    # Doctor preferences
    by_hardcopy = models.BooleanField(default=False)
    by_cd = models.BooleanField(default=False)
    by_usb = models.BooleanField(default=False)
    by_email = models.BooleanField(default=False)

    # For UpdateView to reverse back to after form POST request
    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'pk': self.pk})
