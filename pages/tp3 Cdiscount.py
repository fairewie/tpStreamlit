import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from IPython.display import display
import json
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from database import DataBase
import sqlite3
#import 3. webscraping tp
import sqlalchemy as db

database = DataBase(name_database='data')

chrome_options = Options()
chrome_options.add_argument('--headless')  # Active le mode headless
chrome_options.add_argument('--disable-gpu')  # Désactive le rendu GPU (utile en mode headless)


driver = webdriver.Chrome(options=chrome_options)

BASE_URL = "https://www.but.fr/"
driver.get(BASE_URL)

article_dict = {}

classeBarre = "autocomplete"
classedesarticle = "product"
cookieClasse = 'popin_tc_privacy_button'

def Rechercher_Article(article):
    time.sleep(3)
    cookieclick()
    time.sleep(1)
    selection = driver.find_element(By.ID, classeBarre)
    print(selection)
    selection.send_keys(article)
    time.sleep(1)
    selection.send_keys(u'\ue007')
    time.sleep(3)
    GetArticle()



def cookieclick():
    footer = driver.find_element(By.ID, cookieClasse)
    footer.click()

def GetArticle():
    database.create_table('test3', id=db.String, marque=db.String, prix=db.Integer,image = db.String)
    blocontent = driver.find_element(By.CLASS_NAME, "dp__content")
    ListeArticle = blocontent.find_elements(By.CLASS_NAME, classedesarticle)
    for article in ListeArticle:
        data = {}
        try:
            product_link = article.find_element(By.CLASS_NAME, "product__link.gtm-product")
            product_id = product_link.get_attribute("id")
        except:
            print("ID manquant")
        data["id"] = product_id
        try:
            data["marque"] = article.find_element(By.CLASS_NAME, "overview-title").text
        except:
            print("marque manquante")
        try:
            data["prix"] = article.find_element(By.CLASS_NAME, "overview__prices").text
        except:
            print("prix manquant")
        try:
            data["image"] = article.find_element(By.TAG_NAME, "img").get_attribute("src")
        except:
            print("image manquante")
        article_dict[product_id] = data
        try:
            database.add_row(name_table='test3', **data)
        except Exception as e:
            print(f"Erreur lors de l'ajout des données à la base de données : {e}")

with st.form('Form 1'):
    search = st.text_input('Recherche')
    if st.form_submit_button('Rechercher'):
        Rechercher_Article(search)
        df = pd.DataFrame(article_dict).T
        st.write(df)