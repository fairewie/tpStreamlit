# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ReviewsAllocineItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()
    release = scrapy.Field()
    page = scrapy.Field()

class ReviewsBoursorama(scrapy.Item):
    indice = scrapy.Field()
    cours = scrapy.Field()
    var = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    open_ = scrapy.Field()
    time = scrapy.Field()
    
class ReviewManga(scrapy.Item):
    nom = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field()
    lettre = scrapy.Field()