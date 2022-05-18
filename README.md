# Weather chatbot
## Install
```sh
# create & start virtual env
python -m venv venv
source venv/bin/activate
#install required packages
pip install -U pip setuptools wheel
pip install -U spacy
pip install python-dotenv
#download french model
python -m spacy download fr_core_news_md
```
You need an API key from OpenWeather. Put it in .env file (from .env-example).
## Start
```sh
python3 main.py
```
