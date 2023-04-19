from flask import Flask, request, redirect
from bs4 import BeautifulSoup
from flask_restful import reqparse
import requests
app = Flask(__name__)

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

@app.get('/')
def hello_world():
    return redirect("https://matias.ma/nsfw/", code=302)

@app.route("/<string:sign>", methods=['GET'])
@app.route("/<string:sign>/<string:date>", methods=['GET'])
def horoscope(sign=None, date=None):
    try:
        if(sign != None and date != None):
            if (sign not in signs):
                raise Exception("Sign not found, please refer to your mother because we don't have any documentation for this... Long Live Kotlin")
            response = horoscope_info(sign=signs.index(sign)+1, date=date)
        else:
            response = horoscope_info(sign=signs.index(sign)+1)
        return response, 200
    except Exception as e:
        return {'message': str(e)}, 400

def horoscope_info(sign, date=None):
    """
    Endpoint to parse data from astrology site.
    """
    if(date is None):
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign}")
    else:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={sign}&laDate={date}")
        
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})    
    return data.p.text