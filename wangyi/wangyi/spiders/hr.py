# -*- coding: utf-8 -*-
import scrapy
from wangyi.items import WangyiItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['163.com']
    start_urls = ['http://hr.163.com/position/list.do']

    def parse(self, response):
        tr_list = response.xpath("//table[@class='position-tb']//tr")
        for num, tr in enumerate(tr_list):
            if num % 2 != 0:
                item = WangyiItem()
                item["name"] = tr.xpath(".//td/a/text()").extract_first()
                item["link"] =  tr.xpath(".//td/a/@href").extract_first()
                if item["link"] is not None:
                    item["link"] =response.urljoin(item["link"])
                item["depart"] = tr.xpath(".//td[2]/text()").extract_first()
                item["category"] = tr.xpath(".//td[3]/text()").extract_first()
                item["type"] = tr.xpath(".//td[4]/text()").extract_first()
                item["address"] =  tr.xpath(".//td[5]/text()").extract_first()
                item["num"] = tr.xpath(".//td[6]/text()").extract()
                if item['num']:
                    item['num'] = item['num'][0].strip()
                item["date"] = tr.xpath(".//td[7]/text()").extract_first()
                yield item

        next_url = response.xpath("//div[@class='m-page']/a[last()]/@href").extract_first()
        if next_url != "javascript:void(0)":
            yield scrapy.Request(
                url =  response.urljoin(next_url),
                callback=self.parse
                # dont_filter=False
            )
