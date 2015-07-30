# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('employment_type', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('responsibilities', models.CharField(max_length=255)),
                ('requirement', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('approved', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
