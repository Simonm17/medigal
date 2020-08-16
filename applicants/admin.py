from django.contrib import admin

from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_by', 'created_date',)

    # Can't use list filter on full name because full name is not a field, so use search field
    search_fields = ('first_name', 'last_name',)

    readonly_fields = ('created_date',)

    fieldsets = (
        (None, {'fields': ('prefix', 'first_name', 'last_name', 'suffix')}),
        ('Contact Information', {'fields': ('address', 'telephone', 'email',)}),
        ('Misc.', {'fields': ('notes',)}),
        ('Users', {'fields': ('created_by', 'created_date', 'updated_by', 'updated_date')})
    )

admin.site.register(Applicant, ApplicantAdmin)