# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0007_auto_20160921_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.IntegerField(),
        ),
    ]
