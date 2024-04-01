import scrapy


class ProcuracathoSpider(scrapy.Spider):
    name = "procuraCatho"
    allowed_domains = ["www.catho.com.br"]
    start_urls = ["https://www.catho.com.br/"]

    def parse(self, response):
        pass
