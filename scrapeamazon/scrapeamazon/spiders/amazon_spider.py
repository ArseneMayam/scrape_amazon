# -*- coding: utf-8 -*-
import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    allowed_domains = ['https://www.amazon.ca/']
    start_urls = ['https://www.amazon.ca/gp/most-gifted/amazon-devices/2980422011/ref=zg_mg_pg_2?ie=UTF8&pg=2']

    def parse(self, response):
        title = response.css(".p13n-sc-truncated::text").extract()

        yield {'title': title}
