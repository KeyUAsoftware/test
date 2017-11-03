# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(unique=True)),
                ('payment_type', models.CharField(choices=[(b'stripe', b'Stripe'), (b'paypal', b'PayPal')], max_length=32)),
                ('status', models.CharField(choices=[(b'active', b'Active'), (b'completed', b'Completed')], max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]