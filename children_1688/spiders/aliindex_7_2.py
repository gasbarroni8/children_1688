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

class AliindexSpider(scrapy.Spider):
    name = 'aliindex_7_2'
    allowed_domains = ['1688.com']
    # start_urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=311&rankType=hot&period=week']
    start_urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=127424004&rankType=hot&period=week']

    urls = ['https://index.1688.com/alizs/word/listRankType.json?cat=127424004&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127496001&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1043351&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037003&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037039&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037012&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1048174&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122086001&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037011&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127430003&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127430004&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1042754&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037004&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037649&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1042841&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037010&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037006&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037007&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122704004&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=124188006&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=124196006&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122086002&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037005&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037192&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037648&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1042840&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037008&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=1037009&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=126440003&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=127164001&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122088001&rankType=hot&period=week',
            'https://index.1688.com/alizs/word/listRankType.json?cat=122698004&rankType=hot&period=week']
    custom_settings = {
        'ITEM_PIPELINES': {'children_1688.pipelines.aliIndex_7_2_Pipelines': 300, },
    }

    def parse(self, response):
        print('正在爬取,请稍等......')
        # print(response.text)
        data = json.loads(response.text)
        # print(len(data))
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
                # print(item)
                items.append(item)
            print('爬取完成：' + str(response.url))
            self.urls.remove(response.url)
            if self.urls:
                r = scrapy.Request(url=self.urls[0], callback=self.parse)
                items.append(r)
            return items
        else:
            print('content无数据.....')
            self.urls.remove(response.url)
            if self.urls:
                r = scrapy.Request(url=self.urls[0], callback=self.parse)
                items.append(r)
            return items