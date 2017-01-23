# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0022_auto_20160925_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(max_length=7, choices=[('Мягкий', 'Мягкий'), ('Жесткий', 'Жесткий')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.IntegerField(),
        ),
    ]
