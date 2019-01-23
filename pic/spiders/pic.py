import scrapy
from pic.items import PicItem

class picSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['https://www.trplus.com.tw/']
    start_urls = ['https://www.trplus.com.tw/TR_Gourmet/c/EC_10000053']

    def parse(self, response):
        print("status:"+str(response.status))
        pics = response.xpath('//img[@class="img-fluid"]')
        #print("movies:"+str(movies))
        #print(pics)

        for pic in pics:
            item = PicItem()
            src  = pic.xpath('./@src').extract()
            name  = pic.xpath('./@alt').extract()
            
            if len(name) != 0:
                item['name'] = name[0]

            #print(name)
            #print(src[0])

            #item['name'] = name[0]
            item['src'] = src[0]
            yield item
            