# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    RecruitPostName = scrapy.Field()
    #国家
    CountryName = scrapy.Field()
    #地址
    LocationName = scrapy.Field()
    #事业群
    BGName = scrapy.Field()
    #岗位类别
    CategoryName = scrapy.Field()
    #岗位职责
    Responsibility = scrapy.Field()
    #发布时间
    LastUpdateTime = scrapy.Field()
    PostURL = scrapy.Field()
    ProductName = scrapy.Field()