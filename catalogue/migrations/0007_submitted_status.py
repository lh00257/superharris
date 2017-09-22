# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-08 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_submitted_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitted',
            name='status',
            field=models.IntegerField(choices=[(1, 'To be validated'), (2, 'Accepted'), (3, 'Rejected')], default=1),
        ),
    ]