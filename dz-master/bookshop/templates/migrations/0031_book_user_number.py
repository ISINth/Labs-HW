# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0030_auto_20160926_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_user',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
