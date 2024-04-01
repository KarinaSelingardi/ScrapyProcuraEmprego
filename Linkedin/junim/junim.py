import scrapy
import pandas as pd

class MeuSpider(scrapy.Spider):
    name = 'junim'
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=Desenvolvedor&location=Brasil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0']

    def parse(self, response):
        # Usando o XPath fornecido para extrair o texto do elemento
        titulo_elementos = response.css('h3.base-search-card__title::text').getall()
        link_elementos = response.css('a.base-card__full-link::attr(href)').getall()

        # Verifica se o número de títulos é igual ao número de links
        if len(titulo_elementos) != len(link_elementos):
            self.logger.error("O número de títulos e links não é o mesmo")
            return

        # Criar DataFrame com os dados
        dados = {'Título': titulo_elementos, 'Link': link_elementos}
        df = pd.DataFrame(dados)

        # Salvar DataFrame em um arquivo Excel
        df.to_excel('dados_vagas.xlsx', index=False)

        # Imprimir os títulos e os links extraídos
        for titulo, link in zip(titulo_elementos, link_elementos):
            self.logger.info(f"Título: {titulo}")
            self.logger.info(f"Link: {link}")
