from datetime import datetime

import requests
from bs4 import BeautifulSoup
from flask_api import status
from googletrans import Translator
from markupsafe import escape

from api.settings import HOROSCOPE_DOMAIN_TODAY, HOROSCOPE_DOMAIN_DATE

NATIVE_LANG = 'en'
translator = Translator(service_urls=['translate.google.com', ])

def translate_sign(content: str, target_lang='es') -> str:
  return translator.translate(content, dest=target_lang, src=NATIVE_LANG).text

signs = {
    'aries': {'icon': '♈', 'index': 1},
    'taurus': {'icon': '♉', 'index': 2},
    'gemini': {'icon': '♊', 'index': 3},
    'cancer': {'icon': '♋', 'index': 4},
    'leo': {'icon': '♌', 'index': 5},
    'virgo': {'icon': '♍', 'index': 6},
    'libra': {'icon': '♎', 'index': 7},
    'scorpio': {'icon': '♏', 'index': 8},
    'sagittarius': {'icon': '♐', 'index': 9},
    'capricorn': {'icon': '♑', 'index': 10},
    'aquarius': {'icon': '♒', 'index': 11},
    'pisces': {'icon': '♓', 'index': 12}
}


def get_index_from_sign(sign: str) -> int:
  sign = sign.lower()
  if sign in signs:
      return (signs[sign], signs[sign]['index'])
  raise ValueError("Sign not found in the dictionary of signs.")

def horoscope_info(sign=None, date=None, lang=None):
    """
    Scrap data from astrology site.
    """
    
    if not sign:
        raise ValueError("Sign parameter is required.")
    
    if date:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please provide a date in YYYY-MM-DD format.")
    
    url = HOROSCOPE_DOMAIN_TODAY.format(sign=sign) if not date else HOROSCOPE_DOMAIN_DATE.format(sign=sign, date=date.replace('-', ''))
    res = requests.get(url)
    
    if res.status_code != status.HTTP_200_OK:
        raise Exception("Failed to fetch horoscope information. Status code: {}".format(res.status_code))
    
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})    
    if not data or not data.p:
        raise Exception("Horoscope information not found.")
    
    content_sign = data.p.text
    if lang and lang != NATIVE_LANG:
        content_sign = translate_sign(data.p.text, lang)
    
    return content_sign
  
def get_horoscope(sign=None, date=None, lang=None):
  if not sign:
      raise ValueError("Sign parameter is required.")
  
  sign = sign.lower()
  
  if sign not in signs:
      raise ValueError("Sign not found, please refer to your mother because we don't have any documentation for this... Long Live Kotlin")
  
  sign_object, sign_index = get_index_from_sign(escape(sign))
  content = horoscope_info(sign=sign_index, date=date, lang=lang)
  sign_object['content'] = content
  return sign_object
