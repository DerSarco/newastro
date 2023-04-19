from flask import Flask, request
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

@app.get('/')
def hello_world():
    return "Hello, World!"

@app.post('/')
def horoscope():
    sign = request.args['sign'].lower()
    try:
        if (sign not in signs):
            raise Exception('Wrong sign or day passed. Please refer https://aztro.readthedocs.io/en/latest/ ')
        response = horoscope_info(sign=sign)
        return response, 200
    except Exception as e:
        return {'message': str(e)}, 400

def horoscope_info(sign):
    """
    Endpoint to parse data from astrology site.
    """
    sign = getSign(sign.lower())
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})    
    return data.p.text

def getSign(sign):
    if sign == "aries":
        return 1
    elif sign == "taurus":
        return 2
    elif sign == "gemini":
        return 3
    elif sign == "cancer":
        return 4
    elif sign == "leo":
        return 5
    elif sign == "virgo":
        return 6
    elif sign == "libra":
        return 7
    elif sign == "scorpio":
        return 8
    elif sign == "sagittarius":
        return 9
    elif sign == "capricorn":
        return 10
    elif sign == "aquarius":
        return 11
    elif sign == "pisces":
        return 12