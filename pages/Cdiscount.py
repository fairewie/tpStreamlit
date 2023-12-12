import streamlit as st


articles = []
with st.form('Form 1'):
    search = st.text_input('Recherche')
    if st.form_submit_button('Rechercher'):
        st.write(search)