from django.contrib import admin
from .models import Address, Telephone, Email
# Register your models here.
admin.site.register(Address)
admin.site.register(Telephone)
admin.site.register(Email)