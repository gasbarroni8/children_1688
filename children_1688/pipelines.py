# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

from children_1688.items import Children1688Item, SecondIndexItem


class Children1688Pipeline(object):

    def __init__(self):
        # https://blog.csdn.net/lwgkzl/article/details/82147474  任务 明天早上测试是否可以追加数据 然后写整个页面的爬虫即可
        self.f = open("9.29_Testtwo_Data.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['category1', 'category2', 'showtime', 'purchaseIndex1688', 'purchaseIndexTb', 'supplyIndex' ,'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['purchaseIndexTb'], item['supplyIndex'], item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class secondIndexPipelines(object):

    def __init__(self):
        # https://blog.csdn.net/lwgkzl/article/details/82147474  任务 明天早上测试是否可以追加数据 然后写整个页面的爬虫即可
        self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Top/category2_32.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['category1', 'category2', 'showtime', 'purchaseIndex1688', 'supplyIndex', 'crawl_Time'])


    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['showtime'], item['purchaseIndex1688'], item['supplyIndex'],item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()


class IndustryMarketDown(object):
    def __init__(self):
        self.f = open("/home/chenhang/workplace/crawlFile/HangYeDaPan/Down/IndustryMarketDown.csv", "w")
        self.writer = csv.writer(self.f)
        # self.writer.writerow(['category1', 'category2', 'industry_Type', 'industry_Name', 'purchaseIndex1688', 'supplyIndex', 'crawl_Time'])

    def process_item(self, item, spider):
        list = [item['category1'], item['category2'], item['industry_Type'], item['industry_Name'], item['purchaseIndex1688'], item['supplyIndex'],
                item['crawl_Time']]
        self.writer.writerow(list)
        return item

    def close_spider(self, spider):  # 关闭
        self.f.close()