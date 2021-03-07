# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TiebaPipeline(object):
    def __init__(self):
        self.file_write = open("zhaoliyin.txt", "a",encoding="utf8")
    def process_item(self, item, spider):
        self.file_write.write(json.dumps(dict(item), ensure_ascii=False))
        self.file_write.write("\n")
        print(item)
        return item
