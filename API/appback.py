import uvicorn
from fastapi import FastAPI,Depends
import sqlalchemy as db

from itemadapter import ItemAdapter


class WebcrawlerPipeline:
    def process_item(self, item, spider):
        return item


import sqlalchemy as db

class DataBase():
    def __init__(self, name_database='database'):
        self.name = name_database
        self.url = f"sqlite:///{name_database}.db"
        self.engine = db.create_engine(self.url)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.table = self.engine.table_names()


    def create_table(self, name_table, **kwargs):
        colums = [db.Column(k, v, primary_key = True) if 'id_' in k else db.Column(k, v) for k,v in kwargs.items()]
        db.Table(name_table, self.metadata, *colums)
        self.metadata.create_all(self.engine)
        print(f"Table : '{name_table}' are created succesfully")

    def read_table(self, name_table, return_keys=False):
        table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
        if return_keys:table.columns.keys()
        else : return table


    def add_row(self, name_table, **kwarrgs):
        name_table = self.read_table(name_table)

        stmt = (
            db.insert(name_table).
            values(kwarrgs)
        )
        self.connection.execute(stmt)
        print(f'Row id added')


    def delete_row_by_id(self, table, id_):
        name_table = self.read_table(name_table)

        stmt = (
            db.delete(name_table).
            where(students.c.id_ == id_)
            )
        self.connection.execute(stmt)
        print(f'Row id {id_} deleted')

    def select_table(self, name_table):
        name_table = self.read_table(name_table)
        stm = db.select([name_table])
        return self.connection.execute(stm).fetchall()
# Description of the API
description = """
This is your app description, written in markdown code 

# This is a title 

* This is a bullet point

"""

tag_metadata = [
    {
        "name": "GET",
        "description": "Operations with GET methods. ",
    },
    {
        "name": "TEST",
        "description": "Operations with POST methods. ",
    },
]

app = FastAPI(
    description=description,
    tag_metadata=tag_metadata
)

def get_db():
    db = DataBase()
    try:
        yield db
    finally:
        db.connection.close()


@app.get('/', tags=['GET'])
def index():
    return "Hello World"

@app.get('/square', tags=['TEST'])
def square(n):
    return {n: int(n)**2}


@app.get('/anime', tags=['TEST'])
def animes(lettre: str, db: DataBase = Depends(get_db)):
    animes = db.select_table("animes")
    filtered_animes = [anime for anime in animes if anime.lettre == lettre]

    # Return selected attributes for each anime
    result = [
        {
            "nom": anime.nom,
            "image": anime.image,
            "description": anime.description,
        }
        for anime in filtered_animes
    ]

    return {"animes with the letter": result}

if __name__ == '__main__':
    uvicorn.run(app=app, 
                host='localhost',
                port=8000)