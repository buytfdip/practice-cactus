import scrapy


class PhonesSpider(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['www.backmarket.com']
    start_urls = ['https://www.backmarket.com/en-us/l/smartphones/0744fd27-8605-465d-8691-3b6dffda5969']

    def parse(self, response):
        for item in response.css('a[class="focus:outline-none group md:box-border relative"]'):
            yield {
                "Name": item.css('h2[class="body-1-bold duration-200 line-clamp-1 md:mb-1 md:mt-0 mt-1 normal-case overflow-ellipsis overflow-hidden text-black transition-all"]::text').get().replace('\n      ',''),
                "Price": item.css('span[class="body-2-bold text-black"]::text').get().replace('\n        ','').replace('  $',''),
                "Link": item.css('a[class="focus:outline-none group md:box-border relative"]::attr(href)').get(),
            }
        next_page = response.css('a[aria-label="Navigate to page 2"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)