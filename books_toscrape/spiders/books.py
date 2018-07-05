# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    #extract all the urls which are in index page and send requests but dont follow their urls
    #rules = (Rule(LinkExtractor(),callback='parse_page',follow=False),)

    # extract all the urls which are in index page and send requests, follow their urls too
    #rules = (Rule(LinkExtractor(), callback='parse_page', follow=True),)

    # it will deny domains which are passed in arguments
    # rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parse_page', follow=True),)
    #this will only extact the urls which contans music in their url
    rules = (Rule(LinkExtractor(allow=('music')), callback='parse_page', follow=True),)

    def parse_page(self, response):
        pass
