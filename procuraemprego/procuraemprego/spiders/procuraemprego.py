
from pathlib import Path
import scrapy


class ProcuraempregoSpider(scrapy.Spider):
    name = "procuraemprego"

    start_urls = ["https://empregacampinas.com.br/"]

    def parse(self, response):

        Path ("files/procuraemprego.csv").write_bytes(response.body)

        pass