from flask import Flask, request, redirect
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

@app.get('/')
def hello_world():
    return redirect("https://matias.ma/nsfw/", code=200)

@app.post('/')
def horoscope():
    sign = request.args['sign'].lower()
    try:
        if (sign not in signs):
            raise Exception("Sign not found, please refer to your mother because we don't have any documentation for this... Long Live Kotlin")
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