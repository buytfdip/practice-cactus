##CSS Selectors

#cat pag number to end of url to force pagination
next_page = r'https://www.backmarket.com/en-us/l/smartphones/0744fd27-8605-465d-8691-3b6dffda5969?page=' + str(PhonesSpider.count)

items = response.css('a[class="focus:outline-none group md:box-border relative"]')

name = response.css('h2[class="body-1-bold duration-200 line-clamp-1 md:mb-1 md:mt-0 mt-1 normal-case overflow-ellipsis overflow-hidden text-black transition-all"]::text').get().replace('\n      ','')

price = response.css('span[class="body-2-bold text-black"]::text').get().replace('\n        ','').replace('  $','')

link = response.css('a[class="focus:outline-none group md:box-border relative"]::attr(href)').get()