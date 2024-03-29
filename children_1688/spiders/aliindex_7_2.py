# -*- coding: utf-8 -*-
import json
import time
import scrapy
from children_1688.items import aliIndex_7_2_Item

'''
    陈航
    爬取童装 所有 阿里排行 搜索排行榜 最近7天数据 , 共4个排行榜 每个排行榜50条数据
    用法： scrapy crawl aliindex_7_2 
    此spider为童装热搜榜
    
'''

class aliindex_7_2_spider(scrapy.Spider):
    name = 'aliindex_7_2'
    allowed_domains = ['1688.com']
    start_urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=hot&period=week']
    next = ['311','127424004', '127496001', '1043351', '1037003', '1037039',
            '1037012', '1048174', '122086001', '1037011', '127430003',
            '127430004', '1042754', '1037004', '1037649', '1042841',
            '1037010', '1037006', '1037007', '122704004', '124188006',
            '124196006', '122086002', '1037005', '1037192', '1037648',
            '1042840', '1037008', '1037009', '126440003', '127164001',
            '122088001', '122698004']
    head = 'https://index.1688.com/alizs/word/listRankType.json?cat='
    end = '&rankType=hot&period=week'
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_7_2_Pipelines': 300, },
    }

    def parse(self, response):
        data = json.loads(response.text)
        keywords = []
        indexs = []
        totals = []
        urls = []
        items = []
        if len(data)==2:
            dics = data['content']
            for dic in dics:
                keywords.append(dic.get('keyword'))
                indexs.append(dic.get('index'))
                totals.append(dic.get('total'))
                urls.append(dic.get('url'))
            crawl_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            for i in range(0,len(keywords)):
                item = aliIndex_7_2_Item()
                item['category1'] = '童装'
                item['category2'] = '所有'
                item['attribute_Type'] = '童装热搜榜'
                item['attribute_Name'] = keywords[i]
                item['index'] = indexs[i]
                item['total'] = totals[i]
                item['url'] = urls[i]
                item['crawl_Time'] = crawl_Time
                items.append(item)
            surl = str(response.url)
            start = surl.find('=')
            end = surl.find('&')
            resurl = surl[start+1:end]
            if resurl == '311':
                print('正在更新Spider , 更新数据名称 : aliindex_7_2 1688网站阿里排行搜索排行榜7天热搜榜')
            self.next.remove(resurl)
            if self.next:
                r = scrapy.Request(url=self.head+self.next[0]+self.end, callback=self.parse)
                items.append(r)
            elif len(self.next):
                print('更新Spider完成 , 更新数据名称 : aliindex_7_2 1688网站阿里排行搜索排行榜7天热搜榜')
            return items
        else:
            print('content无数据.....')
            surl = str(response.url)
            start = surl.find('=')
            end = surl.find('&')
            resurl = surl[start + 1:end]
            self.next.remove(resurl)
            if self.next:
                r = scrapy.Request(url=self.head + self.next[0] + self.end, callback=self.parse)
                items.append(r)
            elif len(self.next):
                print('更新Spider完成 , 更新数据名称 : aliindex_7_2 1688网站阿里排行搜索排行榜7天热搜榜')
            return items