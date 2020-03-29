# -*- coding: utf-8 -*-
import scrapy

from ..items import ZhanzhangItem


class ZzSpider(scrapy.Spider):
    name = 'zz'
    allowed_domains = ['http://sc.chinaz.com/tupian/shanshuifengjing.html']
    start_urls = ['http://sc.chinaz.com/tupian/shanshuifengjing.html']

    def parse(self, response):
        img_list = response.xpath('//div[@id="container"]//img')
        for img in img_list:
            src = img.xpath('./@src2').extract_first()
            alt = img.xpath('./@alt').extract_first()
            # 数据不固定 不安全 所以不建议这么写
            # zz = {}
            # zz['src']=src
            # zz['alt']=alt

            zz = ZhanzhangItem(src=src,alt=alt)
            yield zz
