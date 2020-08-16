from django.contrib import admin

from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_by', 'created_date',)
    list_filter = ('suffix',)
    # Can't use list filter on full name because full name is not a field, so use search field
    search_fields = ('first_name', 'last_name',)

    readonly_fields = ('created_date',)

    fieldsets = (
        (None, {'fields': ('prefix', 'first_name', 'last_name', 'suffix')}),
        ('Specialty', {'fields': ('specialty',)}),
        ('Contact Information', {'fields': ('address', 'telephone', 'email',)}),
        ('Preference', {'fields': ('by_hardcopy', 'by_cd', 'by_usb', 'by_email', 'notes')}),
        ('Users', {'fields': ('created_by', 'created_date', 'updated_by', 'updated_date')})
    )


admin.site.register(Doctor, DoctorAdmin)


