# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 12:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_auto_20160820_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequency',
            name='tokens',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
