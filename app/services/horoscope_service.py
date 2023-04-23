from app.utils.signs import SIGNS, get_month_from_sign
from app.models.horoscope import Horoscope
from datetime import datetime

class HoroscopeService:
  def __init__(self, horoscope_repository):
    self.horoscope_repository = horoscope_repository

  def get_horoscope_info(self, sign, date=None, lang=None):
        
    if date:
      current_date = datetime.now().date()
      if datetime.strptime(date, "%Y-%m-%d").date() > current_date:
        raise ValueError("Cannot get horoscope for future date")    
        
    month, sing_extra_info = get_month_from_sign(sign)
    content = self.horoscope_repository.get_horoscope_info(month, date, lang)
    
    if not date:
      """If date is not provided, use today's date"""
      date = datetime.now().strftime("%Y-%m-%d")
    
    return Horoscope(
      sign=sing_extra_info['name'], 
      horoscope=content,
      date=date,
      icon = sing_extra_info['icon'],
      number_month = month
    )