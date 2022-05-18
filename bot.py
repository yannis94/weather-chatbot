import random
import requests
import spacy
from spacy.lang.fr.examples import sentences
from dotenv import dotenv_values

nlp = spacy.load("fr_core_news_md")
config = dotenv_values(".env")
api_key = config['API_KEY']

weather_dictionnary = ["quel temps fait-il à ville", "quel temps fait il a ville", "donne moi la meteo à ville", "donne moi la météo à ville", "quelle est la temperature a ville", "quelle est la température à ville", "quelle température fait-il à ville"]
bot_dictionnary = ["Comment puis-je vous aidez ?", "Que souhaitez vous savoir aujourd'hui", "Avez-vous besoin d'une information ?"]
error_dictionnary = ["Je n'ai pas compris", "Je ne peux vous indiquer uniquement la météo", "Try again dude"]

def ask_user():
    random.seed()
    i = random.randrange(0, len(bot_dictionnary))
    print("Chatbot: {}".format(bot_dictionnary[i]))
    user_question = input("Vous: ")
    if user_question == "quit":
        return "quit"
    question = nlp(user_question.lower())
    return question

def show_error():
    random.seed()
    i = random.randrange(0, len(error_dictionnary))
    print("Chatbot: {}. (Pour quitter, tappez 'quit').\n".format(error_dictionnary[i]))

def get_city(sentence):
    city = ""
    for phrase in weather_dictionnary:
        current = nlp(phrase)
        similarity = current.similarity(sentence)
        if similarity > 0.75:
            city = sentence.ents[0]
            break
    return str(city)

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&lang=fr&appid=" + api_key
    req = requests.get(url)
    if req.status_code != 200:
        print("Chatbot: I can't use Openweaher's API")
        return
    result = req.json()
    return result
    
def display_answer(data):
    descr = data['weather'][0]['description']
    temp_min = data['main']['temp_min'] - 273.15 #kalvin to celcius
    temp_max = data['main']['temp_max'] - 273.15 
    print("Chatbot: Voici la météo du jour.")
    print("Chatbot: Les température iront de {}°C à {}°C aujourd'hui, avec {}.".format(int(temp_min), int(temp_max), descr))
