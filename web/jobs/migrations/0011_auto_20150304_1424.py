# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20150304_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_title',
            new_name='title',
        ),
    ]
