# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150314_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='published',
        ),
    ]
