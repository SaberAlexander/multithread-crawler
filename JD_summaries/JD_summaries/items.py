# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDSummariesItem(scrapy.Item):
	SkuId=scrapy.Field()
	ProductId=scrapy.Field()
	Score5Count=scrapy.Field()
	Score4Count=scrapy.Field()
	Score3Count=scrapy.Field()
	Score2Count=scrapy.Field()
	Score1Count=scrapy.Field()
	ShowCount=scrapy.Field()
	CommentCount=scrapy.Field()
	AverageScore=scrapy.Field()
	GoodCount=scrapy.Field()
	GoodRate=scrapy.Field()
	GoodRateShow=scrapy.Field()
	GoodRateStyle=scrapy.Field()
	GeneralCount=scrapy.Field()
	GeneralRate=scrapy.Field()
	GeneralRateShow=scrapy.Field()
	GeneralRateStyle=scrapy.Field()
	PoorCount=scrapy.Field()
	PoorRate=scrapy.Field()
	PoorRateShow=scrapy.Field()
	PoorRateStyle=scrapy.Field()
	AfterCount=scrapy.Field()
	
	

    # define the fields for your item here like:
    # name = scrapy.Field()
# {"SkuId":3784563,"ProductId":3784563,"Score1Count":268,"Score2Count":79,"Score3Count":267,"Score4Count":614,"Score5Count":8262,"ShowCount":2792,"CommentCount":9490,"AverageScore":5,"GoodCount":8876,"GoodRate":0.936,"GoodRateShow":93,"GoodRateStyle":141,"GeneralCount":346,"GeneralRate":0.036,"GeneralRateShow":4,"GeneralRateStyle":5,"PoorCount":268,"PoorRate":0.028,"PoorRateShow":3,"PoorRateStyle":4,"AfterCount":134}
