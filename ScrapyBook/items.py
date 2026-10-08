# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item

class BookItem(Item):
    authors=Field()
    catalog =Field()
    comments=Field()
    cover=Field()   
    id=Field()
    intrduction=Field()
    isbn=Field()
    name=Field()
    page_name=Field()
    price=Field()
    published_at=Field()
    publisher=Field()
    score=Field()
    tags=Field()
    translators=Field()