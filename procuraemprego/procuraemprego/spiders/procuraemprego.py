from pathlib import Path
import scrapy
import csv


class ProcuraempregoSpider(scrapy.Spider):
    name = "procuraemprego"

    start_urls = ["https://empregacampinas.com.br"]

    def parse(self, response):
        # Seleciona os textos dos links
        texts = response.css('a , .fysyCG ::text').getall()

        # Escreve os textos em um arquivo CSV
        with open("files/empregacampinas03.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for text in texts:
                writer.writerow([text])