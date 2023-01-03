import scrapy

class BrownieSpider(scrapy.Spider):
    name = 'brownie'
    start_urls = ['https://www.brownies.com/food-gifts/bite-size-treats']

    def parse(self,response):
        for products in response.css('div.col-xs-6.col-sm-4.categoryContainerCross'):
            if len(products.css('span.catProdPrice').get().replace('<span class="catProdPrice">\r\n            <span>\r\n            \r\n            \r\n                    $<span>','').replace('</span>\r\n                \r\n            \r\n        </span>\r\n    </span>','')) == 5:
                yield {
                    'Name': products.css('span.catProdName::text').get(),
                    'Price': products.css('span.catProdPrice').get().replace('<span class="catProdPrice">\r\n            <span>\r\n            \r\n            \r\n                    $<span>','').replace('</span>\r\n                \r\n            \r\n        </span>\r\n    </span>',''),
                    'Link': 'https://www.brownies.com/food-gifts/bite-size-treats'+products.css('a').attrib['href'], 
                }
            else:
                yield {
                    'Name': products.css('span.catProdName::text').get(),
                    'Price': 'See Site for Sale Price',
                    'Link': 'https://www.brownies.com/food-gifts/bite-size-treats'+products.css('a').attrib['href'], 
                }                