# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-05-25 02:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juice', '0003_auto_20170525_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='Mmeber_account',
            new_name='Member_account',
        ),
    ]
