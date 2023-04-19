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
        response = horoscope_info(sign=signs.index(sign)+1)
        return response, 200
    except Exception as e:
        return {'message': str(e)}, 400

def horoscope_info(sign):
    """
    Endpoint to parse data from astrology site.
    """
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})    
    return data.p.text