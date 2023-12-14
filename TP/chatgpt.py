
import openai
import bs4
import requests


class TEST:
    def __init__(self, text):
        self.text = text
    
    def openai_translate(self, language):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate the text after in {language}:\n\n{self}\n\n1.",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        response.choices[0].text
        return response.choices[0].text
    
    def openai_text_summary(self):
        reponse = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                "content": f"resume moi le texte suivant: '{self}' Tu fais des liaisons entre les articles avec des mots tel que 'mais', 'donc', 'or', 'par contre', 'en revanche', 'en effet', 'cependant', 'toutefois', 'par ailleurs', 'par contre', 'par contre, 'enfin'"},
                {"role": "user",
                "content": "Voici la liste des actualités à synthétiser :" + actu},
            ],
            max_tokens=100,
            temperature=0.9,
        )

        return reponse['choices'][0]['message']["content"]
    
    def openai_text_generator(self):

        text = requests.get(f'https://www.bing.com/news/search?q={self}').text
        soup = bs4.BeautifulSoup(text, 'html.parser')

        actu = ' '.join(["- Actualité : " + link.text+ ' \n'  for link in soup.find_all('a', 'title')])

        actu.split('\n')
        reponse = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                "content": f"Tu es un rédacteur web qui synthétise l'actualité en 50 mots sur la thématique '{query}' Tu fais des liaisons entre les articles avec des mots tel que 'mais', 'donc', 'or', 'par contre', 'en revanche', 'en effet', 'cependant', 'toutefois', 'par ailleurs', 'par contre', 'par contre, 'enfin'"},
                {"role": "user",
                "content": "Voici la liste des actualités à synthétiser :" + actu},
            ],
            max_tokens=100,
            temperature=0.9,
        )

        return reponse


    def openai_codex(self):
        reponse = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "assistant",
            "content": f"Corrige le code envoyé"},
            {"role": "user",
            "content": "Voici le code à corriger :" + self},
        ],
        max_tokens=200,
        temperature=0.9,
    )

        return reponse

    def openai_image(self):
        response = openai.Image.create(
        prompt=self,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        image_url
        return image_url