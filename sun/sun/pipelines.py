# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SunPipeline(object):



    def process_item(self, item, spider):
        with open("yg.txt",'a', encoding="utf8") as f:
            f.write(json.dumps(dict(item), ensure_ascii=False))
            f.write("\n")
        return item
