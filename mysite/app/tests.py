# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse

from accounts.models import User


class OrderTest(TestCase):

    def setUp(self):
        super(OrderTest, self).setUp()

        self.admin_user = User.objects.create(
            username='admin',
            is_superuser=True,
            is_staff=True,
        )
        self.admin_user.set_password('1234567')
        self.admin_user.save()

    def test_orders(self):
        """

        """

        data = {
            'transaction_id': '',
            'payment_type': '',
            'status': '',
        }

        response = self.client.post(path=reverse('orders'), data=data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='admin', password='1234567')
        response = self.client.post(path=reverse('orders'), data=data, format='json')
        self.assertEqual(response.status_code, 400)

        # we have error in all 3 fields
        for field in response.data.keys():
            self.assertIn(field, data)

        data = {
            'transaction_id': 'bad value',
            'payment_type': 'wrong choice',
            'status': 'wrong choice',
        }

        response = self.client.post(path=reverse('orders'), data=data, format='json')
        self.assertEqual(response.status_code, 400)

        # we have error in all 3 fields
        for field in response.data.keys():
            self.assertIn(field, data)

        data = {
            'transaction_id': 1,
            'payment_type': 'stripe',
            'status': 'active',
        }

        response = self.client.post(path=reverse('orders'), data=data, format='json')
        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.data['transaction_id'], data['transaction_id'])
        self.assertEqual(response.data['payment_type'], data['payment_type'])
        self.assertEqual(response.data['status'], data['status'])

        # we can't send the same transaction_id second time
        response = self.client.post(path=reverse('orders'), data=data, format='json')
        self.assertEqual(response.status_code, 400)

        # fetch orders list
        response = self.client.get(path=reverse('orders'), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
