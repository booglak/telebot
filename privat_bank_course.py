import requests


def get_usd_course():
    req = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    return req.json()[0]['sale']

