import scrapy
from scrapy.linkextractors import LinkExtractor

class XiyoujiSpider(scrapy.Spider):
    name = 'xiyouji'
    allowed_domains = ['www.kulemi.com']
    start_urls = ['http://www.kulemi.com/31579/catalog/']

    def parse(self, response):
         links = LinkExtractor(restrict_xpaths ='/html/body/div[4]/div/div/div/div/div[2]/ul/')
       
         lianjie = links.extract_links(response)
         if lianjie is not None:
            for booksection in lianjie:
                yield scrapy.Request(booksection.url,callback=self.parseSection)


    def parseSection(self,response):
        title = response.xpath('/html/body/div[3]/div[2]/div/div/div[1]/h2/text()').extract()
        content = response.xpath('/html/body/div[3]/div[2]/div/div/div[2]').extract()
        yield {
            'title':title,
            'Content':content
        }
    
        
