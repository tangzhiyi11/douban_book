# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import DoubanBookItem


class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        print item['title']
        print item['rate']
        print item['author']
        print '--------'
        return item
