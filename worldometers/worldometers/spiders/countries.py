import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/'] ## don't add http
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        pass
