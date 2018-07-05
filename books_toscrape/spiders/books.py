# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    #extract all the urls which are in index page and send requests but dont follow their urls
    rules = (Rule(LinkExtractor(),callback='parse_page',follow=False),)
    def parse_page(self, response):
        pass
