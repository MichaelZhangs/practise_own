# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
import time
import json

class CareersSpider(scrapy.Spider):
    name = 'careers'
    allowed_domains = ['tencent.com']
    # start_urls = ['http://careers.tencent.com/search.html?pcid=40001']
    url = "https://careers.tencent.com/tencentcareer/api/post/Query?"
    offset = 1
    # 起始url
    nowTime = time.time()
    timestamp = int(round(nowTime * 1000))
    url_suffix = "timestamp="+str(timestamp)+"cityId=&"+"bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageSize=10&language=zh-cn&area=cn&pageIndex="
    url = url + url_suffix
    start_urls = [url + str(offset)]

    def parse(self, response):
        dic = json.loads(response.text)
        data = dic["Data"]["Posts"]
        for d in data:
            item = TencentItem()
            item["BGName"] = d["BGName"]
            item["CategoryName"]  = d["CategoryName"]
            item["CountryName"] = d["CountryName"]
            item["LastUpdateTime"] = d["LastUpdateTime"]
            item["PostURL"] = d["PostURL"]
            item["ProductName"] = d["ProductName"]
            item["Responsibility"] = d["Responsibility"]
            item["RecruitPostName"] = d["RecruitPostName"]
            item["LocationName"] = d["LocationName"]
            yield item
        if self.offset < 417:
            self.offset += 1

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
