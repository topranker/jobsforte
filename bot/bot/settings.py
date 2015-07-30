# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '/Users/tito/Projects/jobsforte/web')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings'

BOT_NAME = 'bot'

SPIDER_MODULES = ['bot.spiders']
NEWSPIDER_MODULE = 'bot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bot (+http://www.jobsforte.com)'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

ITEM_PIPELINES = {
	'bot.pipelines.BotPipeline': 1000,
}