# -*- coding: utf-8 -*-

from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field

from jobs.models import Job


class BotItem(DjangoItem):
    django_model = Job
