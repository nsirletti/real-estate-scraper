# -*- coding: utf-8 -*-
import scrapy


class LeboncoinSearchresultSpider(scrapy.Spider):
    name = 'leboncoin-searchresult'
    allowed_domains = ['https://www.leboncoin.fr/recherche/?category=10']
    start_urls = ['http://https://www.leboncoin.fr/recherche/?category=10/']

    def parse(self, response):
        pass
