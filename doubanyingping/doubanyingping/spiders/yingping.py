# -*- coding: utf-8 -*-
import scrapy
from doubanyingping.items import *
import json

headers = {
    'Accept': 'application/json',
    'Referer': 'https://m.douban.com/movie/subject/26997663/comments?sort=new_score&start=50',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
next = 0

class YingpingSpider(scrapy.Spider):
    name = 'yingping'
    allowed_domains = ['movie.douban.com']
    # start_urls = ['https://m.douban.com/rexxar/api/v2/movie/26997663/interests?']

    def start_requests(self):
        return [scrapy.Request("https://m.douban.com/rexxar/api/v2/movie/26997663/interests?count=20&order_by=hot&start=0&ck=&for_mobile=1",
                               headers=headers)]

    def parse(self, response):
        global next
        contents = DoubanyingpingItem()
        ajax = json.loads(response.text)['interests'] #
        ct = []
        for i in range(len(ajax)):
            ct.append(ajax[i]['comment']) # contents list
        contents['yingping'] = ct
        yield contents

        next = next+25
        next_page = 'https://m.douban.com/rexxar/api/v2/movie/26997663/interests?count=20&order_by=hot&start={}&ck=&for_mobile=1'.format(next)
        yield scrapy.Request(url=next_page, headers=headers, callback=self.parse, dont_filter=True)