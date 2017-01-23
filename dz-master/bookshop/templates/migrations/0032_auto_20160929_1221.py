# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0031_book_user_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_user',
            old_name='number',
            new_name='count',
        ),
    ]
