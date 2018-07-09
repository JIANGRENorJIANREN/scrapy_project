# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from BooksToScrape.items import *


class BookinfoesSpider(scrapy.Spider):
    name = 'BookInfoes'
    allowed_domains = ['books.toscrape.com']
    #start_urls = ['http://books.toscrape.com/']

    def start_requests(self):
        yield scrapy.Request('http://books.toscrape.com/', callback=self.parse_urls)

    def parse_urls(self, response):
        book_urls = response.css('div.image_container a::attr(href)').extract()

        # 抽取书籍的url
        for i in range(len(book_urls)):
            if book_urls[i].startswith('catalogue'):
                yield scrapy.Request(urljoin('http://books.toscrape.com/', book_urls[i]))
            else:
                yield scrapy.Request(urljoin('http://books.toscrape.com/catalogue/', book_urls[i]))

        # 抽取下一页的url
        next_page = response.css('li.next a[href*=page]::attr(href)').extract_first()
        if next_page:
            if next_page.startswith('catalogue'):
                yield scrapy.Request(urljoin('http://books.toscrape.com/', next_page), callback=self.parse_urls)
            else:
                yield scrapy.Request(urljoin('http://books.toscrape.com/catalogue/', next_page), callback=self.parse_urls)

    def parse(self, response):
        bookinfo = BookstoscrapeItem()
        bookinfo['name'] = response.css('div.col-sm-6.product_main h1::text').extract_first()
        bookinfo['price'] = response.css('div.col-sm-6.product_main p.price_color::text').extract_first()
        infos = response.css('tr td::text').extract()
        bookinfo['UPC'] = infos[0]
        bookinfo['avalibility'] = infos[-2]
        bookinfo['number_of_reviews'] = infos[-1]
        yield bookinfo

