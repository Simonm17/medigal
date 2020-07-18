from django.db import models
from users.models import User

class Address(models.Model):
    ADDRESS_TYPE = [
        ('PHYSICAL', 'Physical'),
        ('MAILING', 'Mailing'),
    ]
    address_type = models.CharField(max_length=8, choices=ADDRESS_TYPE, default='PHYSICAL')
    address = models.CharField(max_length=250)
    suite_number = models.CharField(max_length=15, verbose_name='suite number', blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField(verbose_name='Postal Code')

    def __str__(self):
        return f'{self.address[0:8]}.. {self.city[0:5]}, {self.state} {self.zipcode}'


class Telephone(models.Model):
    TYPE = [
        ('H', 'Home'),
        ('W', 'Work'),
        ('S', 'School'),
        ('Mo', 'Mobile'),
        ('Ma', 'Main'),
        ('HF', 'Home Fax'),
        ('WF', 'Work Fax'),
        ('P', 'Pager'),
        ('O', 'Other'),
    ]
    number = models.IntegerField()
    type = models.CharField(max_length=2, choices=TYPE, default='Ma')

    def __str__(self):
        num = str(self.number)
        if len(num) == 10:
            return f'{num[:3]}-{num[3:6]}-{num[6:]}'
        elif len(num) == 11:
            return f'({num[0]}) {num[1:4]}-{num[4:7]}-{num[7:]}'
        else:
            return num


class Email(models.Model):
    email = models.EmailField(max_length=250)
    def __str__(self):
        return self.email


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    ssn = models.IntegerField(verbose_name="Social Security Number", unique=True, blank=True, null=True)
    # Null has no effect on ManyToManyField
    address = models.ManyToManyField(Address, blank=True)
    telephone = models.ManyToManyField(Telephone, blank=True)
    email = models.ManyToManyField(Email, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        abstract = True

class Applicant(Person):
    pass

class Doctor(Person):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="updated_by")
    updated_date = models.DateTimeField(auto_now=True, null=True)


