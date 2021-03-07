# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        print(response.url)
        dt_list = response.xpath("//div[@class='mc']/dl/dt")
        print(dt_list)
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath(".//a/text()").extract_first()
            em_list = dt.xpath("./following::dd[1]/em")
            for em in em_list:
                item["s_href"] = em.xpath("./a/@href").extract_first()
                item["s_cate"] = em.xpath("./a/text()").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = "https:"+item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        dont_filter=True,
                        meta={
                            "item":deepcopy(item)
                        }
                    )


    def parse_book_list(self, response):#解析列表页
        item = response.meta["item"]
        li_list = response.xpath("//div[@id='J_goodsList']/ul/li")
        for li in li_list:
            item["book_img"] = li.xpath(".//div[@class='p-img']/a/img/@src").extract_first()
            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()
            item["book_author"] = li.xpath(".//span[@class='p-bi-name']/a/@title").extract()
            item["publish_store"] = li.xpath(".//span[@class='p-bi-store']/a/@title").extract_first()
            item["publish_time"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first()
            item["book_price"] = li.xpath(".//div[@class='p-price']/text()")
            print(item)
            yield item