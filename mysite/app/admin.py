# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'payment_type', 'status', 'created')
    list_filter = ('status',)


admin.site.register(Order, OrderAdmin)
