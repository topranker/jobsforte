# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150129_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_level',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
