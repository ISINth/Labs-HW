# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0032_auto_20160929_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_user',
            old_name='count',
            new_name='number',
        ),
    ]
