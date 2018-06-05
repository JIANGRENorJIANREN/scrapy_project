# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import *
from maoyan.settings import *
from urllib.parse import urljoin
from pprint import PrettyPrinter


class Top100Spider(scrapy.Spider):
    name = 'top100'
    allowed_domains = ['maoyan.com']
    # start_urls = ['http://maoyan/board/4?offset=0']
    start_urls = ['http://maoyan.com/board/4']
    offset = 0

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=DEFAULT_REQUEST_HEADERS, callback=self.parse)

    def parse(self, response):
        seed_url = 'http://maoyan.com/board/4?offset='
        item = MaoyanItem()
        item['name'] = response.css('div.board-item-main div.board-item-content div.movie-item-info p.name a::text').extract()
        item['star'] = response.css('div.board-item-content div.movie-item-info p.star::text').extract()
        item['releasetime'] = response.css('div.board-item-content div.movie-item-info p.releasetime::text').extract()
        yield item

        self.offset = self.offset + 10
        if self.offset < 100:
            yield scrapy.Request(url='http://maoyan.com/board/4?offset='+str(self.offset), headers=DEFAULT_REQUEST_HEADERS)