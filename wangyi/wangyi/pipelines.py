# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class WangyiPipeline(object):
    def __init__(self):
        self.write_file = open("wangyi.txt","a",encoding="utf8")

    def process_item(self, item, spider):
        self.write_file.write(json.dumps(dict(item),ensure_ascii=False))
        self.write_file.write("\n")
        return item
