# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from showdata.models import house
from showdata.models import newhouse
class BkhouseItem(DjangoItem):
    django_model = house
    pass

class BknewhouseItem(DjangoItem):
    django_model = newhouse
    pass
# class BkhouseItem(scrapy.Item):
#     title = scrapy.Field()
#     msg = scrapy.Field()
#     price = scrapy.Field()
#     per_meter = scrapy.Field()
#     place = scrapy.Field()
#     pass
