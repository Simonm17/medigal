from django.db import models
from users.models import User
from django.urls import reverse


class Address(models.Model):
    ADDRESS_TYPE = [
        ('Physical', 'Physical'),
        ('Mailing', 'Mailing'),
    ]
    address_type = models.CharField(max_length=8, choices=ADDRESS_TYPE, default='PHYSICAL')
    address = models.CharField(max_length=250)
    suite_number = models.CharField(max_length=15, verbose_name='suite number', blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField(verbose_name='Postal Code')

    def __str__(self):
        return f'{self.address}, {self.city[0:5]}, {self.state} {self.zipcode}'
    
    def get_absolute_url(self):
        return reverse('address_detail', kwargs={'pk': self.pk})

class Telephone(models.Model):
    TYPE = [
        ('H', 'Home'),
        ('W', 'Work'),
        ('S', 'School'),
        ('C', 'Cell'),
        ('M', 'Main'),
        ('F', 'Fax'),
        ('P', 'Pager'),
        ('O', 'Other'),
    ]
    type = models.CharField(max_length=2, choices=TYPE, default='M')
    number = models.IntegerField()
    extension = models.IntegerField(blank=True, null=True)

    def __str__(self):
        num = str(self.number)
        if len(num) == 10:
            return f'({num[:3]}) {num[3:6]}-{num[6:]}'
        elif len(num) == 11:
            return f'{num[0]} ({num[1:4]})-{num[4:7]}-{num[7:]}'
        else:
            return num


class Email(models.Model):
    email = models.EmailField(max_length=250)
    def __str__(self):
        return self.email


class Person(models.Model):

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
    prefix = models.CharField(max_length=10, choices=PREFIX, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, choices=SUFFIX, blank=True)
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


