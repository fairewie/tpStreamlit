import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsBoursorama
from datetime import date

class BoursoramaSpider(scrapy.Spider):
    name = "boursorama"
    allowed_domains = ["www.boursorama.com"]
    start_urls = ["https://www.boursorama.com/bourse/actions/palmares/france/page-1"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)

    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[1:]

        for indices in liste_indices:
            item = ReviewsAllocineItem()

            #indice boursier
            try:
                item['indice'] = liste_indices.css('a.c-link::text')[0].get()
            except:
                item['indice'] = 'None'

            #indice cours de l'action
            try:
                item['cours'] = liste_indices.css('span.c-instrument--last::text')[0].get()
            except:
                item['cours'] = 'None'

            #Variation de l'action
            try:
                item['var'] =  liste_indices.css('span.c-instrument--instant-variation::text')[0].get()
            except:
                item['var'] = 'None'

            #Valeur la plus haute
            try:
                item['high'] =  liste_indices.css('span.c-instrument--high::text')[0].get()
            except:
                item['high'] = 'None'

            #Valeur la plus basse
            try:
                item['low'] = liste_indices.css('span.c-instrument--low::text')[0].get()
            except:
                item['low'] = 'None'

            #Valeur d'ouverture
            try:
                item['open_'] = liste_indices.css('span.c-instrument--open::text')[0].get()
            except:
                item['open_'] = 'None'

            #Date de la collecte
            try:
                item['time'] = date.today()
            except:
                item['time'] = 'None'

            yield item