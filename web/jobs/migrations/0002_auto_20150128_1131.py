# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approval', models.CharField(default=b'NO', max_length=3, choices=[[b'YES', b'Approved'], [b'NO', b'Not Approved']])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='job',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 11, 31, 34, 151605, tzinfo=utc), verbose_name=b'Date Scraped', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='approved',
            field=models.ForeignKey(to='jobs.Approval'),
            preserve_default=True,
        ),
    ]
