# -*- coding: utf-8 -*-
import scrapy


class WikipediaCountrySpider(scrapy.Spider):
    name = 'wikipedia_country'
    start_urls = ['https://en.wikipedia.org/wiki/Visa_requirements_for_Indian_citizens']

    custom_settings = {
        'FEED_URI' : 'WikiCountrylinks%(time)s.json',
        'FEED_FORMAT': 'json',
        # 'FEED_EXPORT_FIELDS': ['Country', 'Visa requirement', 'Allowed stay', 'Notes (excluding departure fees)']
    }

    def parse(self, response):
        image = response.xpath('.//div[@class = "thumb tnone"]/div/a/img/@src').extract()
        legend_color = []
        field = []
        visa_type = []
        stay = []
        detail = []
        for legend_xpath in response.xpath('.//div[@class = "thumb tnone"]/div/div[@class = "thumbcaption"]/div[@class = "legend"]/span/@style').re('background-color: ?#?[A-Za-z0-9]*;'):
            legend_color.append((legend_xpath.split(':')[1])[:-1])
        for f in response.xpath('.//div[@class = "thumb tnone"]/div/div[@class = "thumbcaption"]/div[@class = "legend"]/text()').getall():
            field.append(f[1:])
        head = response.xpath('.//div[@id="mw-content-text"]/div/table[1]/tbody/tr/th/text()').getall()
        country_name = response.xpath('.//div[@id="mw-content-text"]/div/table[1]/tbody/tr/td[1]/a[1]/text()').getall()
        for t in response.xpath('.//div[@id="mw-content-text"]/div/table[1]/tbody/tr/td[2]'):
            x = t.css('td ::text').get()
            if x != None:
                visa_type.append(x)
            elif x == None:
                y = t.xpath('./td[2]/span/text()').get()
                if y != None:
                    visa_type.append(y)
            else:
                pass
        visa_type = [x for x in visa_type if x != '\n']
        for s in response.xpath('.//div[@id="mw-content-text"]/div/table[1]/tbody/tr/td[3]'):
            x = s.css('td ::text').get()
            if x is not None:
                stay.append(x)
            else:
                stay.append('NA')
        for d in response.xpath('.//div[@id="mw-content-text"]/div/table[1]/tbody/tr'):
            s = d.xpath('./td[4]').xpath('string()').get()
            if s is '\n' or s is None:
                detail.append('None here')
            else:
                detail.append(s)
        detail.pop(0)
        visa = {
            head[0] : country_name,
            head[1] : visa_type,
            head[2] : stay,
            head[3] : detail
        }
        legend = dict(zip(legend_color, field))
        yield {
            'map' : image,
            'legend' : legend,
            'visa' : visa
        }
