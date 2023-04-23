
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from app.utils.status_code import Status
from app.utils.translate import NATIVE_LANG, text_translate


class HoroscopeRepository:
  
  MAIN_PATH_URL         = "https://www.horoscope.com/us/horoscopes/general/"
  
  def _get_horoscope_url_today(self, sign):
    """ Get horoscope url today. """
    return f"{self.MAIN_PATH_URL}horoscope-general-daily-today.aspx?sign={sign}"
  
  def _get_horoscope_url_date(self, sign, date):
    """ Get horoscope url date. """
    return f"{self.MAIN_PATH_URL}horoscope-archive.aspx?sign={sign}&laDate={date.replace('-', '')}"
  
  def get_horoscope_info(self, month, date, lang):
    """ 
    Get horoscope info from the https://www.horoscope.com. 
    
    Args:
      sign (int): El número de mes del zodiaco para el cual se desea obtener la información del horóscopo.
      date (str): La fecha para la cual se desea obtener la información del horóscopo (en formato YYYY-MM-DD).
      lang (str): El idioma al que se desea traducir el contenido del horóscopo. Si no se proporciona, se devolverá en el idioma nativo.
    
    Returns:
      str: El contenido del horóscopo para el signo y fecha proporcionados, traducido al idioma solicitado si se proporciona.
    
    Raises:
      ValueError: Si el parámetro sign es nulo.
      ValueError: Si el parámetro date no es nulo y no está en formato YYYY-MM-DD.
      requests.exceptions.RequestException: Si ocurre un error al realizar la solicitud HTTP.
      HoroscopeInfoNotFoundError: Si la información del horóscopo no se encuentra en la respuesta HTTP.
          
    """
    if not month:
        raise ValueError("Sign parameter is required.")
    
    if date:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please provide a date in YYYY-MM-DD format.")
    
    url = self._get_horoscope_url_today(month) if not date else self._get_horoscope_url_date(month, date)    
    res = requests.get(url)
        
  
    if res.status_code != Status.HTTP_OK:
        raise Exception("Failed to fetch horoscope information. Status code: {}".format(res.status_code))
    
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})    
    
    if not data or not data.p:
        raise Exception("Horoscope information not found.")
      
    horoscope = data.p.text
    if lang and lang != NATIVE_LANG:
        horoscope = text_translate(data.p.text, lang)
    
    return horoscope