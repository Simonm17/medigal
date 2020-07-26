from django.db import models
from users.models import User
from django.urls import reverse
from contacts.models import Person

class Doctor(Person):
    """
    created/updated fields are on child model instead of parent Person model due to conflicting reverse query name for other child models e.g. Applicant
    """
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    # Putting blank & null = True for updated fields 
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="updated_by", blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_created_date(self):
        return f'Created on {self.created_date} by {self.created_by}'

    def get_updated_date(self):
        return f'Updated on {self.updated_date} by {self.updated_by}'

    # For UpdateView to reverse back to after form POST request
    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'pk': self.pk})
