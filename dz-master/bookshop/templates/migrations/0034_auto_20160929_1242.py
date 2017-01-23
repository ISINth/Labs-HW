# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0033_auto_20160929_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_user',
            name='number',
            field=models.IntegerField(),
        ),
    ]
