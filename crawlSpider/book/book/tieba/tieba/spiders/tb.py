# -*- coding: utf-8 -*-
import scrapy

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&ie=utf-8&pn=0']

    def parse(self, response):
        div_list = response.xpath("//ul[@id='thread_list']/li//div[@class='t_con cleafix']")
        for div in div_list:
            item = {}
            item["title"] = div.xpath(".//div[@class='threadlist_lz clearfix']/div/a/@title").extract_first()
            item["content_url"] = "http://tieba.baidu.com" + div.xpath(".//div[@class='threadlist_lz clearfix']/div/a/@href").extract_first()
            # item["author"] = div.xpath(".//span[@class='tb_icon_author']/@title").extract_first()
            item["answ_num"] = div.xpath(".//div/span/text()").extract_first()
            item["create_time"] = div.xpath(".//span[@class='pull-right is_show_create_time']/text()").extract_first()

            print(item)
            yield scrapy.Request(
                item["content_url"],
                callback=self.parse_detail,
                dont_filter=True,
                meta={
                    "item": item,
                    'dont_redirect': True,
                    'handle_httpstatus_list': [302]
                      }
            )
        next_url =  response.xpath("//div[@id='frs_list_pager']/a[@class='next pagination-item ']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                url="http:" + next_url,
                dont_filter=True,
                meta={
                    'dont_redirect': True,
                    'handle_httpstatus_list': [302]

                },
                callback=self.parse
            )

    def parse_detail(self,response):

        item = response.meta["item"]
        url = response.xpath("//div[@class='d_author']/ul[@class='p_author']/li/div/a/@href").extract_first()
        if url is not None:
            yield scrapy.Request(
                url= "http://tieba.baidu.com" + url,
                callback=self.parse_detail_tieba,
                dont_filter=True,
                meta={
                    "item":item,
                    'dont_redirect': True,
                    'handle_httpstatus_list': [302]
                }
            )

    def parse_detail_tieba(self, response):
        item = response.meta["item"]
        item["tieba_img"] = response.xpath("//div[@id='j_userhead']/a/img/@src").extract_first()
        item["tieba_age"] = response.xpath("//div[@class='userinfo_userdata']/span[2]/text()").extract_first().split(":")[-1]
        item["tieba_count"] = response.xpath("//div[@class='userinfo_userdata']/span[4]/text()").extract_first().split(":")[-1]
        print(item)
        yield item