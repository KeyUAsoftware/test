# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from app.models import Order
from app.serializers import OrderSerializer


class OrdersView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    ordering = ('-created',)
