# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from mysite.model_choices import *


class Order(models.Model):
    transaction_id = models.IntegerField(unique=True)
    payment_type = models.CharField(max_length=32, choices=PAYMENT_TYPES)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id
