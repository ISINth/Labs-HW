# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0023_auto_20160925_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus scelerisque est sem, et accumsan ipsum bibendum vel. Nullam placerat condimentum sapien, vitae auctor lacus congue sit amet. Suspendisse potenti. Aenean dignissim interdum urna sed ornare. Duis neque mi, mollis et posuere eget, lobortis sit amet nunc. Suspendisse erat tellus, ullamcorper sit amet diam suscipit, convallis porttitor est. Aliquam eu ex ultrices, elementum nibh et, convallis erat.'),
        ),
    ]
