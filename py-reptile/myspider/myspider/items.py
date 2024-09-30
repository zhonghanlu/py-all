# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UbuntuItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()


class DoubanItem(scrapy.Item):
    film_name = scrapy.Field()
    film_author = scrapy.Field()
    film_actor = scrapy.Field()
    film_category = scrapy.Field()
    film_score = scrapy.Field()
