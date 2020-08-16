from django.contrib import admin

from .models import Address, Telephone, Email


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'city', 'state', 'zipcode',)
    list_filter = ('city', 'zipcode',)

    search_fields = ('address1', 'address2')

    fieldsets = (
        ('Address', {'fields': ('address_type', 'address1', 'unit_type', 'address2', 'city', 'state', 'zipcode')}),
        
    )

admin.site.register(Address, AddressAdmin)
admin.site.register(Telephone)
admin.site.register(Email)