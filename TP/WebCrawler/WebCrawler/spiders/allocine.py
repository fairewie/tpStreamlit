import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsAllocineItem


class AllocineSpider(scrapy.Spider):
    name = "allocine"
    allowed_domains = ["www.allocine.fr"]
    start_urls = ["https://www.allocine.fr/film/meilleurs"]


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_allocine)


    def parse_allocine(self, response):
        liste_film = list_films = response.css('li.mdl')


        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = ReviewsAllocineItem()

            # Nom du film
            try:
                item['title'] = list_films.css('a.meta-title-link::text')[0].get()
            except:
                item['title'] = 'None'

            # Lien de l'image du film
            try:
                item['img'] = list_films.css('img::attr(src)')[0].get()
            except:
                item['img'] = 'None'


            # Auteur du film
            try:
                item['author'] = list_films.css('a.blue-link::text')[0].get()
            except:
                item['author'] = 'None'

            # Durée du film
            try:
                item['time'] = list_films.css('div.meta-body-item.meta-body-info::text')[0].get()
            except:
                item['time'] = 'None'

            # Genre cinématographique
            try:
                item['genre'] = list_films.css('div.meta-body-item.meta-body-info span::text')[1].get()
            except:
                 item['genre'] = 'None'

            # Score du film
            try:
                item['score'] = list_films.css('span.stareval-note::text')[0].get()
            except:
                item['score'] = 'None'

            # Description du film
            try:
                item['desc'] = list_films.css('div.content-txt ::text')[0].get()
            except:
                item['desc'] = 'None'

            # Date de sortie
            try:
                item['release'] = list_films.css('span.date::text')[0].get()
            except:
                item['release'] = 'None'


            yield item