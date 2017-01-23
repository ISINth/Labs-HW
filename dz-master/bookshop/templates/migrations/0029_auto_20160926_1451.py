# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0028_auto_20160925_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='book_user',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
