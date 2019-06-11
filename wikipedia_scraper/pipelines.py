# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import csv
# import json
# from wikipedia_scraper import settings

# class JsonWriterPipeline(object):

#     def open_spider(self, spider):
#         self.file = open('wikilinks.jl', 'w')

#     def close_spider(self, spider):
#         self.file.close()

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item

# def write_to_csv(item):
#     writer = csv.writer(open('wikilinks.csv', 'w'), lineterminator='\n')
#     writer.writerow([item[key] for key in item.keys()])

# class WriteToCsv(object):
#         def process_item(self, item, spider):
#             write_to_csv(item)
#             return item

class WikipediaScraperPipeline(object):
    def process_item(self, item, spider):
        return item
