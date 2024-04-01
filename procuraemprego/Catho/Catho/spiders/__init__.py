# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from pathlib import Path
import scrapy


class ProcuraempregoSpider(scrapy.Spider):
    name = "Catho"

    start_urls = ["https://www.catho.com.br/"]

    def parse(self, response):
        Path ("new/catho.xlsx").write_bytes(response.body)

        pass
