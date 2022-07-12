from django.contrib import admin
from .models import Organization

# Register your models here.


class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
        'donation_url',
        'logo',
    )

    ordering = ('name',)


admin.site.register(Organization, OrganizationAdmin)
