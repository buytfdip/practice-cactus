#CSS Seletors

next_page = response.css('a[aria-label="Navigate to page 2"]::attr(href)').get()

items = response.css('a[class="focus:outline-none group md:box-border relative"]')

name = response.css('h2[class="body-1-bold duration-200 line-clamp-1 md:mb-1 md:mt-0 mt-1 normal-case overflow-ellipsis overflow-hidden text-black transition-all"]::text').get().replace('\n      ','')

price = response.css('span[class="body-2-bold text-black"]::text').get().replace('\n        ','').replace('  $','')

link = response.css('a[class="focus:outline-none group md:box-border relative"]::attr(href)').get()