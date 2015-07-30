# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20150130_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='responsibilities',
        ),
        migrations.AddField(
            model_name='job',
            name='source',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='employment_type',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_level',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='requirement',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(default=b'Competitive', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='specialization',
            field=models.CharField(max_length=130, null=True, blank=True),
            preserve_default=True,
        ),
    ]
