# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanyingpingPipeline(object):
    def process_item(self, item, spider):
        if item['yingping']:
            #for comment in item['yingping']:
            #    return comment
            return item
        else:
            raise DropItem("Missing price in %s" % item)