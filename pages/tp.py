import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json
from bs4 import BeautifulSoup

st.set_page_config(
    page_title="tp", page_icon="nasus.ico",layout="wide"
    )


article_dict = {}

def scraping_bdm(art):
    for article in art:

        id = article.get('id')

        title = article.find('h3').text.replace('\xa0', ' ')            # Title
        
        try:image = article.find('img')['data-lazy-src']                # Image
        except:image = None
       
        try:link = article.find('a')["href"]                            # Link
        except:link = article.parent['href']

        try:theme = article.find('span', 'favtag').text                 # Catégorie
        except:theme = article.find_previous('h2').text
        
        date = article.find('time')['datetime'].split('T')[0]           # Date
        
        article_dict[id] = { 'title' :title, 'date'  :date, 'link':link, 'image' :image, 'categorie' : theme }
    return article_dict


url = 'https://www.blogdumoderateur.com/'

query = '?s='



# on = st.toggle('Theme sombre', False)
# if on:
#     st.markdown("""
#     <style>
#     body {
#         background-color: #1a1a1a;
#         color: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)
# else:
#     st.markdown("""
#     <style>
#     body {
#         background-color: white;
#         color: black;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# st.title("td test")


nb_page = st.slider('Nombre de page', 1, 15)
articles = []
with st.form('Form 1'):
    search = st.text_input('Recherche')
    if st.form_submit_button('Rechercher'):
        for i in range(int(nb_page)):
            response = requests.get(url+query+search+'&page='+str(i))
            soup = BeautifulSoup(response.content, 'html.parser')
            articles += soup.find_all('article')
        # response = requests.get(url+query+search)
        # soup = BeautifulSoup(response.content, 'html.parser')
        # articles = soup.find_all('article')
        st.write(articles)
        st.write(scraping_bdm(articles))
        df = st.write(pd.DataFrame(article_dict).T)
        st.write(df)
df = pd.DataFrame(article_dict)

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)


if search:
    st.download_button(
        label="télécharger le csv",
        data=csv,
        file_name='test.csv',
        mime='text/csv',
    )