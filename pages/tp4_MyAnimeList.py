import streamlit as st
import requests

st.set_page_config(page_title="MyAnimeList", page_icon="nasus.ico", layout="wide")

lettres_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



st.title("MyAnimeList")

st.header("Rechercher par lettre")
st.write("Saisir une lettre pour afficher les animes commençant par cette lettre")


lettre_selectionnee = st.selectbox("Sélectionnez une lettre", lettres_alphabet)


with st.form('Form 1'):
    if st.form_submit_button('Rechercher'):
        st.write(f"Lettre sélectionnée : {lettre_selectionnee}")
        #fetch api avec la lettre
        api_url = f"http://localhost:8000/anime?lettre={lettre_selectionnee}"
        response = requests.get(api_url)
        st.write(response.json())