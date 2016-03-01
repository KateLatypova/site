# -*- coding: utf-8 -*-
from django.contrib import admin
from visits.models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'uri', 'visits']
    list_filter = ['ip_address', 'uri']
    search_fields = ['ip_address', 'uri']

admin.site.register(Visit, VisitAdmin)
