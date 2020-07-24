from django.db import models
from users.models import User
from django.urls import reverse
from contacts.models import Person

class Doctor(Person):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    # Putting blank & null = True for updated fields 
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="updated_by", blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    # For UpdateView to reverse back to after form POST request
    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'pk': self.pk})