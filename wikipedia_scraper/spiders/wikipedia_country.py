# -*- coding: utf-8 -*-
import scrapy


class WikipediaCountrySpider(scrapy.Spider):
    name = 'wikipedia_country'
    start_urls = ['https://en.wikipedia.org/wiki/Visa_requirements_for_Indian_citizens']

    custom_settings = {
        'FEED_URI' : 'WikiCountrylinks%(time)s.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_FIELDS': ['map', 'legend']
    }

    def parse(self, response):
        image = response.xpath('.//div[@class = "thumb tnone"]/div/a/img/@src').extract()
        legend_color = []
        field = []
        for legend_xpath in response.xpath('.//div[@class = "thumb tnone"]/div/div[@class = "thumbcaption"]/div[@class = "legend"]/span/@style').re('background-color: ?#?[A-Za-z0-9]*;'):
            legend_color.append((legend_xpath.split(':')[1])[:-1])
        for f in response.xpath('.//div[@class = "thumb tnone"]/div/div[@class = "thumbcaption"]/div[@class = "legend"]/text()').getall():
            field.append(f[1:]) 
        legend = dict(zip(legend_color, field))
        yield {
            'map' : image,
            'legend' : legend
        }
