import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsBoursorama
from datetime import datetime
from WebCrawler.pipelines import DataBase
import sqlalchemy as db

class BoursoramaSpider(scrapy.Spider):
    name = "boursorama"
    allowed_domains = ["www.boursorama.com"]
    start_urls = ["https://www.boursorama.com/bourse/actions/palmares/france/page-1"]
    database = DataBase('database')
    try:
        database.create_table('boursorama',
                                   indice = db.String,
                                   cours = db.String,
                                   var  = db.String,
                                   high  = db.String,
                                   low  = db.String,
                                   open_  = db.String,
                                   time  = db.String
                                   )
    except:
        pass
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)

    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[3:]

        for indices in liste_indices:
            item = ReviewsBoursorama()

            #indice boursier
            try:
                item['indice'] = indices.css('a.c-link::text').get()
            except:
                item['indice'] = 'None'

            #indice cours de l'action
            try:
                item['cours'] = indices.css('span.c-instrument--last::text').get()
            except:
                item['cours'] = 'None'

            #Variation de l'action
            try:
                item['var'] =  indices.css('span.c-instrument--instant-variation::text').get()
            except:
                item['var'] = 'None'

            #Valeur la plus haute
            try:
                item['high'] =  indices.css('span.c-instrument--high::text').get()
            except:
                item['high'] = 'None'

            #Valeur la plus basse
            try:
                item['low'] = indices.css('span.c-instrument--low::text').get()
            except:
                item['low'] = 'None'

            #Valeur d'ouverture
            try:
                item['open_'] = indices.css('span.c-instrument--open::text').get()
            except:
                item['open_'] = 'None'

            #Date de la collecte
            try:
                item['time'] = datetime.today()
            except:
                item['time'] = 'None'

            self.database.add_row('boursorama', 
                                   indice = item['indice'],
                                   cours = item['cours'],
                                   var  = item['var'],
                                   high  = item['high'],
                                   low  = item['low'],
                                   open_  = item['open_'],
                                   time  = item['time'])
            yield item