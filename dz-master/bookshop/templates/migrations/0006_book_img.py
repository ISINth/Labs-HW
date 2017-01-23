# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0005_auto_20160921_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
