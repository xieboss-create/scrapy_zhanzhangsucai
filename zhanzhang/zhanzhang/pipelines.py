# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ZhanzhangPipeline(object):
    # 在爬虫文件开始执行之前 执行的方法
    def open_spider(self, spider):
        self.fp = open('zz.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    # 执行完爬虫文件之后 调用的方法
    def close_spider(self, spider):
        self.fp.close()


import urllib.request


class DownLoadImagePipeline(object):
    def process_item(self, item, spider):
        src = item['src']
        alt = item['alt']

        filename = './images/' + alt + '.jpg'

        urllib.request.urlretrieve(url=src, filename=filename)

        return item
