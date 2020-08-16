from django.contrib import admin

from .models import Company, Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('requester', 'request_date', 'reviewed')
    list_filter = ('reviewed', 'requester')

    search_fields = ('requester',)
    ordering = ('request_date',)
    readonly_fields = ('request_date',)

    fieldsets = (
        ('Request', {'fields': ('requester', 'request_date', 'company_name', 'company_telephone', 'company_website',)}),
        ('Staff Actions', {'fields' : ('notes', 'reviewed', 'accepted', 'denied')})
    )

    filter_horizontal = ()

# Register your models here.
admin.site.register(Company)
admin.site.register(Request, RequestAdmin)