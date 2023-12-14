import streamlit as st
import requests

st.set_page_config(page_title="MyAnimeList", page_icon="nasus.ico", layout="wide")

lettres_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



st.title("MyAnimeList")

st.header("Rechercher par lettre")
st.write("Saisir une lettre pour afficher les animes commençant par cette lettre")


lettre_selectionnee = st.selectbox("Sélectionnez une lettre", lettres_alphabet)



st.markdown(
    """
    # MyAnimeList
    
    <iframe src="http://localhost:8000/docs#" width="800" height="600"></iframe>
    """,
    unsafe_allow_html=True,
)