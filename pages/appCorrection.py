import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="correction", page_icon="nasus.ico",layout="wide"
    )


st.title("My first Title")

st.markdown("""
# Titre
## Sous-titre
```
            print('Hello World')
```          
"""
)

# Sous-titre
st.subheader("Subheader")

# Afficher des éléments sur la page
st.write("Bonjour tout le monde !")

df = pd.read_json('bdm.json').T
if st.checkbox('Afficher le dataframe'):
    st.write(df)

# Création de colonnes
col1, col2 = st.columns(2)

with col1:
    # Graphique avec matplotlib
    fig, ax = plt.subplots()
    ax.hist(df.categorie)
    st.pyplot(fig)

with col2:
    # Graphique avec plotly.expres
    st.plotly_chart(px.histogram(df.categorie))

theme = st.selectbox('Sélectionnez le thème : ', df.categorie.value_counts().index)

st.write(theme, len(df[df.categorie == theme].categorie))

text = st.text_input('Tape your text')
st.title(text)


with st.form('Form 1'):
    name = st.text_input('Tape your name')
    age = st.slider('Select your age : ', 0, 100)

    if st.form_submit_button('Send Form'):
        st.write('Your name : %s'%(name))
        st.write(f'Your age : {age}')

