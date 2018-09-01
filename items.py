# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WbacityItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    xiaoqu = scrapy.Field()
    address = scrapy.Field()
    show_img = scrapy.Field()
    category = scrapy.Field()
    add_info = scrapy.Field()
    lease = scrapy.Field()
    phone = scrapy.Field()
    big_img = scrapy.Field()
    orient = scrapy.Field()
    big_info = scrapy.Field()
    pass


