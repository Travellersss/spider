# -*- coding: utf-8 -*-
import scrapy
from imgspider.items import ImgspiderItem

class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['enrz.com']
    start_urls = ['http://www.enrz.com/beauty/cover-girl']


    def parse(self, response):
        links=response.xpath('//h4[contains(@class,"list-thumbnail-title")]/a/@href').extract()
        for link in links:

            yield scrapy.Request(link,callback=self.parse_item)

        url=response.xpath('//div[@class="pagination"]/a/@href').extract()


        yield scrapy.Request(url[1],callback=self.parse)
    def parse_item(self,response):
        item=ImgspiderItem()
        item['title']=response.xpath('//div[@id="content"]/h2/text()').extract()
        item['imgurls']=response.xpath('//div[@id="content"]/p/img/@src').extract()

        yield item