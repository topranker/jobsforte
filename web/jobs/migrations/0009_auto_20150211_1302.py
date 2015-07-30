# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20150211_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_level',
            field=models.CharField(default=b'None', max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
    ]
