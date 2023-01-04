import scrapy


class PhonesSpider(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['www.backmarket.com']
    start_urls = ['https://www.backmarket.com/en-us/l/smartphones/0744fd27-8605-465d-8691-3b6dffda5969']

    def parse(self, response):

