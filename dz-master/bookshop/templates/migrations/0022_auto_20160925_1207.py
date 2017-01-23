# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0021_auto_20160924_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.IntegerField(choices=[('Мягкий', 'Мягкий'), ('Жесткий', 'Жесткий')], max_length=7),
        ),
    ]
