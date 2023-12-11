import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="app", page_icon="nasus.ico",layout="wide"
    )

st.title("Streamlit App")

#sidebar link



st.subheader("Subheader")
st.write("Write")

df = pd.read_json("bdm.json").T

if(st.checkbox("Show Dataframe")):
    st.write(df)

    
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.hist(df.categorie)
    st.pyplot(fig)

with col2:
    st.plotly_chart(px.histogram(df.categorie))


theme = st.selectbox("selectionner le theme", df.categorie.value_counts().index)
st.write(theme, len(df[df.categorie == theme].categorie))

text = st.text_input("text input")
st.title(text)

with st.form('Form 1'):
    name = st.text_input('Enter your name')
    age = st.slider('Enter your age : ', 1, 100)

    if st.form_submit_button('Submit'):
        st.write(f'Hello {name}, you are {age} years old')
