import scrapy
from scrapy import Request
from WebCrawler.items import ReviewManga
from datetime import datetime
from WebCrawler.pipelines import DataBase
import sqlalchemy as db


class MangaSpider(scrapy.Spider):
    name = "manga"
    allowed_domains = ["myanimelist.net"]
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


    database = DataBase('database')
    try:
        database.create_table('anime',
                                   nom = db.String,
                                   image = db.String,
                                   description  = db.String,
                                   lettre = db.String,
                                   )
    except:
        pass

    def start_requests(self):
        for letter in self.letters:
            url = f"https://myanimelist.net/manga.php?letter={letter}"
            yield Request(url=url, callback=self.parse_manga, meta={'lettre': letter})

    def parse_boursorama(self, response):
        lettre = response.meta['lettre']
        liste_manga = response.css('tr')[8:]
        for manga in liste_manga:
            item = ReviewManga()

            #indice boursier
            try:
                item['nom'] = manga.css('strong::text').get()
            except:
                item['nom'] = 'None'

            #indice cours de l'action
            try:
                item['image'] = manga.css('img::attr(data-src)').get()
            except:
                item['image'] = 'None'

            #Variation de l'action
            try:
                item['description'] = manga.css('div.pt4::text').get()
            except:
                item['description'] = 'None'

            try:
                item['lettre'] = lettre
            except:
                item['lettre'] = 'None'

            # self.database.add_row('boursorama', 
            #                        indice = item['nom'],
            #                        cours = item['image'],
            #                        var  = item['description'],
            # )
            yield item