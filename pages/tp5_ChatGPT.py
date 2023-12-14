import streamlit as st
import requests
from TP.WebCrawler.WebCrawler.pipelines import TextProcessor 

st.set_page_config(page_title="Chatgpt prompt", page_icon="nasus.ico", layout="wide")

st.title("Chatgpt")

text_processor_instance = TextProcessor()

user_input = st.text_input("/help pour afficher les commandes")


if user_input == "/help":
    # Affichez les commandes d'aide
    st.write("/help - Affiche les commandes disponibles")
    st.write("/translate + 'texte'- traduit le 'texte' envoyer")
    st.write("/imagine + 'texte'- Génère une image à partir du 'texte' envoyé.")
    st.write("/code + 'texte'- retourne le code corrigé à partir de 'texte' envoyer")

    st.write("/actu + 'theme'- Fait un résumé de 5 actualités à partir du 'theme' envoyé")
    st.write("/json + 'url' - Retourne le contenu de l'url envoyé sous forme de json.")

elif user_input.startswith("/translate"):
    text_after_imagine = user_input.split("/translate", 1)[-1].strip()
    st.write("Vous avez saisi translate avec :", text_after_imagine)
    st.write(text_processor_instance.openai_translate(text_after_imagine,"français"))

elif user_input.startswith("/imagine"):
    text_after_imagine = user_input.split("/imagine", 1)[-1].strip()
    st.write("Vous avez saisi imagine avec :", text_after_imagine)
    image_url = text_processor_instance.openai_image(text_after_imagine)
    st.image(image_url, caption="Image générée avec OpenAI")

elif user_input.startswith("/code"):
    text_after_imagine = user_input.split("/code", 1)[-1].strip()
    st.write("Vous avez saisi code avec :", text_after_imagine)
    st.write(text_processor_instance.openai_codex(text_after_imagine))



elif user_input.startswith("/actu"):
    text_after_imagine = user_input.split("/actu", 1)[-1].strip()
    st.write("Vous avez saisi actu avec :", text_after_imagine)
    st.write(text_processor_instance.openai_text_generator(text_after_imagine))


elif user_input.startswith("/json"):
    text_after_imagine = user_input.split("/json", 1)[-1].strip()
    st.write("Vous avez saisi json avec :", text_after_imagine)


else:
    # Affichez autre chose en fonction de l'entrée utilisateur
    st.write("Vous avez saisi :", user_input)