# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from WbaCity.items import WbacityItem


class WbaSpider(CrawlSpider):
    name = 'Wba'
    # allowed_domains = ['58.com/']
    start_urls = ['http://xa.58.com/chuzu/sub/l94/b2/']

    rules = (
        Rule(LinkExtractor(allow=r'np\d+/'), callback='parse', follow=True),
    )


    def parse(self, response):
        li_list = response.xpath('//ul[@class="listUl"]//li')
        print('长度时候：',len(li_list))
        for li in li_list:
            item = WbacityItem()
            item['name'] = li.xpath('./div[@class="des"]/h2/a/text()').extract_first().strip()
            item['price'] = li.xpath('./div[@class="listliright"]/div[@class="money"]/b/text()').extract_first().strip()
            item['area'] = li.xpath('./div[@class="des"]/p[@class="room"]/text()').extract_first().strip()
            item['xiaoqu'] = li.xpath('./div[@class="des"]/p[@class="add"]/a[2]/text()').extract_first()
            item['address'] = li.xpath('./div[@class="des"]/p[@class="add"]/a[1]/text()').extract_first().strip()
            item['show_img'] = li.xpath('./div[@class="img_list"]/a/img/@src').extract_first().strip()
            # item['category'] = li.xpath('./div[@class="des"]/div[@class="jjr"]/*/text()').extract()
            f_url = li.xpath('.//div[@class="des"]/h2/a/@href').extract_first()
            if f_url.startswith('xa.58'):
                item['category'] = li.xpath('./div[@class="des"]/div[@class="jjr"]/span[@class=" jjr_par"]//text()').extract()
            else:
                item['category'] = li.xpath('./div[@class="des"]/p[@class="geren"]//text()').extract()
            url='http:'+f_url
            # print('第二个页面是：',url)
            # yield item
            yield scrapy.Request(url=url,callback=self.xia_page,meta={'item':item})


    def xia_page(self,response):
        # print("进入第二个页面了")
        item = response.meta['item']
        item['add_info'] = response.xpath('//ul[@class="f14"]/li[5]/span[2]/a/text()').extract_first().strip()
        item['lease'] = response.xpath('//div[@class="house-pay-way f16"]/span[2]/text()').extract_first().strip()
        item['phone'] = response.xpath('//div[@class="house-chat-phone"]/span/text()').extract_first()
        item['big_img'] = response.xpath('//div[@class="basic-top-bigpic pr "]/img/@src').extract_first().strip()
        item['orient'] = response.xpath('//ul[@class="f14"]/li[3]/span/text()').extract_first().strip()
        item['big_info'] = response.xpath('//div[@class="house-word-introduce f16 c_555"]/ul/li[2]/span//text()').extract()
        # print(item).strip()
        yield item



