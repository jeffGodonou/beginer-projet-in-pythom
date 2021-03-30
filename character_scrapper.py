import scrapy
from scrapy.crawler import CrawlerProcess

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d\'animation']

    def parse(self, response):
        for link in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {'character': link.css('a ::text').extract_first()}

process = CrawlerProcess(settings={
    "FEEDS": {
        "characters.json": {"format": "json"},
    },
})

process.crawl(BlogSpider)
process.start() # the script will block here until the crawling is finished
