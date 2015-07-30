# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150128_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Approval',
        ),
    ]
