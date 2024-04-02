from pathlib import Path
import scrapy
import csv


class ProcuraCathoSpider(scrapy.Spider):
    name = "procuraCatho"

    start_urls = ["https://catho.com.br/"]

    def parse(self, response):
        # Seleciona os textos dos links
        texts = response.css('a ::text').getall()

        # Escreve os textos em um arquivo CSV
        with open("dados_extraidos/Catho06.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for text in texts:
                writer.writerow([text])

