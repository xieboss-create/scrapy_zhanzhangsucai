# -*- coding: utf-8 -*-
import scrapy

from ..items import ZhanzhangItem


class ZzSpider(scrapy.Spider):
    name = 'zz'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/tupian/shanshuifengjing.html']

    base_url = 'http://sc.chinaz.com/tupian/shanshuifengjing'
    page = 1

    def parse(self, response):
        img_list = response.xpath('//div[@id="container"]//img')
        for img in img_list:
            src = img.xpath('./@src2').extract_first()
            alt = img.xpath('./@alt').extract_first()
            # 数据不固定 不安全 所以不建议这么写
            # zz = {}
            # zz['src']=src
            # zz['alt']=alt

            zz = ZhanzhangItem(src=src, alt=alt)
            yield zz

        if self.page < 5:
            self.page = self.page + 1
            url = self.base_url + '_' + str(self.page) + '.html'
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)
