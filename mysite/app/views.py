# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from app.models import Order
from app.serializers import OrderSerializer


class OrdersView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    ordering = ('-created',)
