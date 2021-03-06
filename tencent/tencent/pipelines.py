# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TencentPipeline(object):
    def process_item(self, item, spider):
        with open("tencent.json","a", encoding="utf8") as fr:
            fr.write(json.dumps(dict(item),ensure_ascii=False))
            fr.write("\n")
        return item
