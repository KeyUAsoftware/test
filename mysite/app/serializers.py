# -*- coding: utf-8 -*-

from rest_framework import serializers

from app.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'transaction_id', 'payment_type', 'status')
