# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-31 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecount',
            old_name='cont',
            new_name='count',
        ),
    ]