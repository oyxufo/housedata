# -*- coding: utf-8 -*-
import itertools

import scrapy
from pyquery import PyQuery as pq
import json
import pandas as pd
from bkhouse.items import BknewhouseItem

class NewhousespiderSpider(scrapy.Spider):
    name = 'newhousespider'
    allowed_domains = ['ke.com']
    start_urls = ['https://wh.fang.ke.com/loupan/pg1']

    # 爬取某网页
    def get_one_page(self, response):
        # result = requests.get(url)
        currenthouse = response.xpath('//div[@class="resblock-desc-wrapper"]')

        for house_item in currenthouse:
            newhouse = BknewhouseItem()
            newhouse['title'] = house_item.xpath("div[@class='resblock-name']/a[@class='name ']/text()").extract()
            # print(newhouse['title'])
            newhouse['place'] = house_item.xpath("a[@class='resblock-location']/text()").extract()[1].replace('\r','').replace('\n','').replace('\t','')
            newhouse['size'] = house_item.xpath("a[@class='resblock-room']/span[@class='area']/text()").extract_first()
            str=''
            list = house_item.xpath("a[@class='resblock-room']/span/text()").extract()
            newhouse['msg']=str.join(itertools.chain(*list))
            newhouse["per_meter"] = house_item.xpath("div[@class='resblock-price']/div[@class='main-price']/span[@class='number']/text()").extract_first()
            if newhouse["per_meter"] == '价格待定':
                newhouse["per_meter"] = 0
            # print(newhouse["size"])
            print(newhouse['per_meter'])
            yield newhouse

    def parse(self, response):
        for i in range(1, 101):
            url = 'https://wh.fang.ke.com/loupan' + f'/pg{i}/'
            print(url)
            # get_one_page(url, str[12:-1])
            yield scrapy.Request(url=url, callback=self.get_one_page,meta={
                 'dont_redirect': True,
                 'handle_httpstatus_list': [302]
                })

        pass
