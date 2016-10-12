# -*- coding: utf-8 -*-
import scrapy
import re
from douban_book.items import DoubanBookItem


class BookSpider(scrapy.Spider):
    name = "book"
    start_urls = [
        'https://www.douban.com/doulist/1264675/',
    ]
    URL = 'https://www.douban.com/doulist/1264675/?start=PAGE&sort=seq&sub_type='

    def parse(self, response):
        item = DoubanBookItem()
        selector = scrapy.Selector(response)
        books = selector.xpath('//div[@class="bd doulist-subject"]')
        for book in books:
            title = book.xpath('div[@class="title"]/a/text()').extract()[0]
            rate = book.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            author = re.search('<div class="abstract">(.*?)<br', book.extract(), re.S).group(1)
            title = title.replace(' ', '').replace('\n', '')
            author = author.replace(' ', '').replace('\n', '')
            item['title'] = title
            item['rate'] = rate
            item['author'] = author
            yield item
        next_page = selector.xpath('//span[@class="next"]/link/@href').extract()
        if next_page:
            next = next_page[0]
            print next
            yield scrapy.http.Request(next, callback=self.parse)