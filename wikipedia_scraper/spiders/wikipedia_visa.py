# -*- coding: utf-8 -*-
import scrapy

class WikiVisa(scrapy.Item):
    country = scrapy.Field()
    link = scrapy.Field()


class WikipediaVisaSpider(scrapy.Spider):
    name = 'wikipedia_visa'
    start_urls = ['https://en.wikipedia.org/w/index.php?title=Category:Visa_requirements_by_nationality', 
                'https://en.wikipedia.org/w/index.php?title=Category:Visa_requirements_by_nationality&pagefrom=Turkey%0AVisa+requirements+for+Turkish+citizens#mw-pages']

    custom_settings = {
        'FEED_URI' : 'Wikilinks%(time)s.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORT_FIELDS': ['country', 'link']
    }

    def parse(self, response):
        for country_group in response.xpath('.//div[@class = "mw-category-group"]'):
            for country in country_group.css('ul'):
                for c in country.css('li'):
                    info = WikiVisa()
                    info['country'] = c.css('li ::text').get()
                    info['link'] = c.css('li ::attr(href)').get()
                    yield info