# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0027_auto_20160925_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_user',
            name='user',
            field=models.IntegerField(),
        ),
    ]
