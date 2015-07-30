# -*- coding: utf-8 -*-


from jobs.models import Job


class BotPipeline(object):
    def process_item(self, item, spider):
        #import ipdb
        #ipdb.set_trace();
        item.save()
        return item
