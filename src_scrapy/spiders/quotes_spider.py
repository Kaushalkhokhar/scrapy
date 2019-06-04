import scrapy
from scrapy.http import FormRequest
from ..items import SrcScrapyItem

'''class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        # this makes a request to folowing url. and will run callback method in respose of the given request
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # this is callback method attached with response object. Runs when response cames.
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)'''

# this is alternativeg of above method that has default call back parse(). parse is scrapys defualt call back.
'''class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)'''

# Example of extracting requried data from url given.
'''class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):

        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            yield {
                'text': text,
                'author': author,
                'tags': tags,
            }'''

'''class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2 # this is not needed in method 1
    start_urls = [
        'http://quotes.toscrape.com/page/1/',        
    ]

    def parse(self, response):
        items = SrcScrapyItem()

        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tags = quote.css('div.tags a.tag::text').extract()


            items['text'] = text
            items['author'] = author
            items['tags'] = tags
            yield items
        
        # to extract data from every page to follow every page
       
        # Method 1:
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
            # yield response.follow(next_page, self.parse)
        
        # Method 2: Also known as pagination
        next_page = 'http://quotes.toscrape.com/page/' + str(QuotesSpider.page_number) + '/'
        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1        
            yield response.follow(next_page, self.parse)'''

# to store data to container here it is items. Which is in ..items.py file
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2 # this is not needed in method 1
    start_urls = [Ama
        'http://quotes.toscrape.com/login',        
    ]

    def parse(self, response):
        # to get login using scrapy
        csrf_token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': csrf_token, # This field we get from insect element > network > login > header and find Form data
            'username': 'kaushal',
            'password': 'sdfgsgfg'
        }, callback=self.start_scrapping)

    def start_scrapping(self, response):
        items = SrcScrapyItem()

        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tags = quote.css('div.tags a.tag::text').extract()


            items['text'] = text
            items['author'] = author
            items['tags'] = tags
            yield items
        
        # to extract data from every page to follow every page
       
        # Method 1:
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
            # yield response.follow(next_page, self.parse)
        
        # Method 2: Also known as pagination
        next_page = 'http://quotes.toscrape.com/page/' + str(QuotesSpider.page_number) + '/'
        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1        
            yield response.follow(next_page, self.start_scrapping)


# to crrate json file of extracted data we ahve to write scrapy crawl <name of spider> -o <filename>.<format> here format can be json, xml
# to store data to databse we need to create pipline. to do that in settings.py uncomment pipline. 