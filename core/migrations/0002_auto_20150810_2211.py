# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zipcode',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='neighborhood',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
