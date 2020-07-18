from django.contrib import admin
from .models import Address, Telephone, Email, Doctor
# Register your models here.
admin.site.register(Address)
admin.site.register(Telephone)
admin.site.register(Email)
admin.site.register(Doctor)