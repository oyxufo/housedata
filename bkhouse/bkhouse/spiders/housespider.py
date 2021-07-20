# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
import json
import pandas as pd
from bkhouse.items import BkhouseItem

class HousespiderSpider(scrapy.Spider):
    name = 'housespider'
    allowed_domains = ['ke.com']
    start_urls = ['https://wh.ke.com/ershoufang/pg1/']
    columns = ['title', 'msg', 'price', 'per_meter']

    # 爬取某网页
    def get_one_page(self, response):
        # result = requests.get(url)
        doc = pq(response.text)
        ul = doc('.sellListContent')
        divs = ul.children('.clear .info.clear').items()
        count = 0

        for div in divs:
            house = BkhouseItem()
            count += 1
            house['title'] = div.children('.title a').text()
            house['place'] = response.meta['place']
            house['msg'] = div.children('.address .houseInfo').text()
            house['price'] = div.children('.address .priceInfo .totalPrice span').text()
            house['per_meter'] = div.children('.address .priceInfo .unitPrice').attr('data-price')
            house['size'] = format(float(house['price'])*10000/float(house['per_meter']),'.2f')
            # print(house)
            yield house

    def parse(self, response):
        doc = pq(response.text)
        alls = doc('[data-role="ershoufang"] .CLICKDATA').items()
        # pagess = doc('.page-box.fr')
        # print(pagess)
        # pages = pagess.children('[data-page]').items()
        # for page in pages:
        #    print(page)
        for area in alls:
            print(area.attr.href[:-3])
            for i in range(1, 101):
                url = 'https://wh.ke.com' + area.attr.href[:-3] + f'pg{i}/'
                print(url)
                str = area.attr.href[12:-4]
                # get_one_page(url, str[12:-1])
                yield scrapy.Request(url=url, callback=self.get_one_page,meta={'place':str})

        pass
