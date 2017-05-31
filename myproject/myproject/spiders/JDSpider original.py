#coding=utf8
'''
Created on Mar 3, 2017

@author: fate
'''
import scrapy
from urlparse import urljoin
import uniout
#from myproject.items import JDItem
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst, MapCompose, Join
from myproject.items import JDItem
from scrapy_splash import SplashRequest
# import profile
import re
import time

class  JDSpider(scrapy.Spider):
    name='jditems'
    def start_requests(self):
        urls = ['https://search.jd.com/Search?keyword=耐克&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=6&wq=耐克&page=1&s=1&click=0',
                 'https://search.jd.com/Search?keyword=耐克&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=6&wq=耐克&page=3&s=51&click=0',
                  ]

        for i in range(100):
            a=5+i*2
            b=110+i*60
            str_a=str(a)
            str_b=str(b)
            next_page='https://search.jd.com/Search?keyword=耐克&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=6&wq=耐克&page='+str_a+'&s='+str_b+'&click=0'
            urls.append(next_page)
            for url in urls:
                yield scrapy.Request(url, callback=self.parse)
                
    def parse(self,response):
        ls=response.xpath('//li[@data-sku]/@data-sku').extract()
        for urltail in ls:
            url=urljoin('https://item.jd.com/1665416.html',urltail)+'.html'        
            #url=urljoin('https://item.jd.com',urltail)  
            yield SplashRequest(url,callback=self.item_parse,args={'wait':0.5}) 

        # next_pages=[]
        # a=range(1,201,2)
        # b=range(1,5939,60)
         
        # for i in range(100):
        #     str_a=str(a[i])
        #     str_b=str(b[i])
        #     print str_a,str_b
        
            
           # time.sleep(10)
            
            
        # for new_url in next_pages:       
            
    def item_parse(self,response):

        item_url=response.url
        pattern=re.compile(r'\d+')
        idlist=pattern.findall(item_url)
        for i in idlist:
            item_id=i
        profile=response.xpath('//div[@class="sku-name"]/text()').extract_first()
        if profile is not None:
        	profile=profile.strip()
        
        shop=response.xpath('//div[@class="name"]/a/text()').extract_first()
        if shop is None:
            shop_temp=response.xpath('//div[@class="name"]')
            shop=shop_temp.xpath('string(.)').extract_first()
        if shop is not None:
            shop="".join(shop.split())

        shop_url=response.xpath('//div[@class="name"]/a/@href').extract_first()
        
        temp=response.xpath('//em[@class="u-jd"]')# []为非京东自营返回值
        flag=temp.xpath('string(.)').extract_first()
        if flag is not None:
            flag=flag.strip()

        price=response.xpath('//span[@class="p-price"]/span[@class]/text()').extract_first() 
        if price is None:
            price=response.xpath('//span[@class="p-price"]/span[@class="p-price"]/span[@class]/text()').extract_first()

        jd_item=JDItem()
        jd_item['item_url']=item_url
        jd_item['item_id']=item_id
        jd_item['profile']=profile
        jd_item['shop']=shop
        jd_item['shop_url']=shop_url
        jd_item['flag']=flag
        jd_item['price']=price

        return jd_item
    
#         l = ItemstLoader(item=JDitem(), response=response):
#         l.add_value('item_id',item_id)
#         l.add_value('item_url',item_url)
#         l.add_xpath('profilr','//div[@class="sku-name"]/text()')
#         l.add_xpath('shop','//div[@class="name"]/a/text()')
#         l.add_value('flag',flage)
#         l.add_xpath('price','//span[@class="p-price"]/span[@class]/text()')
#         l.add_xpath('price','//span[@class="p-price"]/span[@class]/text()')
#         return l.load_item()


# class ItemstLoader(ItemLoader):

#     default_output_processor = TakeFirst()

#     name_in = MapCompose(unicode.title)
#     name_out = Join()

#     price_in = MapCompose(unicode.strip)
        # yield {
        #  'item_url':item_url,
        #  'item_id':item_id,
        #  'profile':profile,
        #  'shop':shop,
        #  'shop_url':shop_url,
        #  'flag':flag,
        #  'price':price,
        #      }

        
