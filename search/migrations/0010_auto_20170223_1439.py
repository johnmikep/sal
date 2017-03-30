# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20170125_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedsearch',
            name='name',
            field=models.CharField(default='Unsaved Search 2017-02-23 22:39:22.057488+00:00', max_length=100),
        ),
        migrations.AlterField(
            model_name='searchfieldcache',
            name='search_model',
            field=models.CharField(choices=[('Machine', 'Machine'), ('Facter', 'Facter'), ('Condition', 'Condition'), ('External Script', 'External Script'), ('Application Inventory', 'Application Inventory'), ('Application Version', 'Application Version')], default='AND', max_length=254, verbose_name='Search item'),
        ),
        migrations.AlterField(
            model_name='searchrow',
            name='search_models',
            field=models.CharField(choices=[('Machine', 'Machine'), ('Facter', 'Facter'), ('Condition', 'Condition'), ('External Script', 'External Script'), ('Application Inventory', 'Application Inventory'), ('Application Version', 'Application Version')], default='AND', max_length=254, verbose_name='Search item'),
        ),
    ]