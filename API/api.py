import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd



# Description of the API
description = """
This is your app description, written in markdown code 

# This is a title 

* This is a bullet point

"""

# Tags for documentation
tag_metadata = [
    {
        "name": "GET",
        "description": "Operations with GET methods. ",
    },
    {
        "name": "POST",
        "description": "Operations with POST methods. ",
    },
]

# Create the app
app = FastAPI(
    title= "My First API",
    description=description,
    openapi_tags=tag_metadata
)


# Create a first endpoint
@app.get("/")
def index():
    return "Hello World"


# Create a GET endpoint
@app.get("/user_name", tags=['GET'])
def user_name(name:str='Joe'):
    return "Bonjour " + name



# Create a GET endpoint
@app.get("/square", tags=['GET'])
def square(number:int=0):
    message = {
        'Text' : "La valeur au carré de " + str(number) + " est " + str(number*number),
        "Value" : number*number
    }
    return message


# Create a base model
class Article(BaseModel):
    title: str
    content: str
    author: str


# Create a POST endpoint
@app.post("/article", tags=['POST', 'GET'])
def create_article(article: Article):
    df = pd.read_csv('articles.csv')

    data_article = {
        'id': len(df) +1,
        "title": article.title,
        "content": article.content,
        "author": article.author
    }

    data = pd.DataFrame(data_article, index=[0])

    df = pd.concat([df, data], ignore_index=True)
    df.to_csv('articles.csv', index=False)
    return df.to_json()


# Create a first endpoint
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)