# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-16 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='diff',
            field=models.FileField(upload_to=b''),
        ),
    ]