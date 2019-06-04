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