# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookstoscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    UPC = scrapy.Field()
    avalibility = scrapy.Field()
    number_of_reviews = scrapy.Field()

