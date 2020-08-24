import scrapy
from scrapy.http import FormRequest
from ..items import AmazonItem

# to store data to container here it is items. Which is in ..items.py file
class AmazoneSpider(scrapy.Spider):
    name = "amazon"
    page_number = 2 # this is not needed in method 1
    start_urls = [
        'https://www.amazon.in/s?k=mobiles&rh=n%3A976419031%2Cn%3A1805560031&dc&qid=1559622381&rnid=3576079031&ref=sr_nr_n_2',        
    ]

    def parse(self, response):
        '''# to get login using scrapy
        csrf_token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': csrf_token, # This field we get from insect element > network > login > header and find Form data
            'username': 'kaushal',
            'password': 'sdfgsgfg'
        }, callback=self.start_scrapping)'''

    #def start_scrapping(self, response):
        items = AmazonItem()

        for mobiles in response.css('.s-include-content-margin'):
            product_name = mobiles.css('.a-color-base.a-text-normal').css('::text').extract()
            product_price = mobiles.css('.a-price-whole').css('::text').extract()
            product_imagelink = mobiles.css('.s-image::attr(src)').extract()


            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_imagelink'] = product_imagelink
            yield items
        
        # to extract data from every page to follow every page
       
        # Method 1:
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
            # yield response.follow(next_page, self.parse)
        
        # Method 2: Also known as pagination
        next_page = 'https://www.amazon.in/s?k=mobiles&i=electronics&rh=n%3A976419031%2Cn%3A1805560031&dc&page=' + str(AmazoneSpider.page_number) + '&qid=1559626657&rnid=3576079031&ref=sr_pg_2'
        if AmazoneSpider.page_number < 4:
            AmazoneSpider.page_number += 1        
            yield response.follow(next_page, self.parse)

# what is user agent?
# when we go to any websites it asks the identity of browser(crome/mozila).
# that identity of browser is know as user agent
# so to crawl a data, we use google user agent instead of our self
# and we rotate a user agent so amazon thigs that different google browser is acessing our site
# to do this we need to install scrapy-user-agents by "pip install scrapy-user-agents"
# and add middleware file to settings.py file as already added
# DOWNLOADER_MIDDLEWARES = {
    #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#}

# what is IP address?
# location/address of our computer
# so using someone else Ip known as proxy
# so to install "pip install scrapy_proxy_pool"
# to know mroe aboout it fo to "https://github.com/hyan15/scrapy-proxy-pool"
# we need to add to things as below to settings.py file
# PROXY_POOL_ENABLED = True
#      and
# DOWNLOADER_MIDDLEWARES = {
    # ...
    #'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    #'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
#}