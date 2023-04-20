import json

import pytest
from flask_api import status

# trunk-ignore(trunk/ignore-does-nothing)
from api.app import app
from api.utils.horoscope_utils import translate_sign, get_index_from_sign, horoscope_info
app.testing = True

# Path: tests/test_api.py

def test_root_path():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
  
def test_get_horoscope_info_with_sign_method_post():
  client = app.test_client()
  
  sign = 'aries' 
  date = '2022-04-20'
  lang = 'es'
    
  response = client.post(
    '/',  
    data=json.dumps({'sign': sign, 'date': date, 'lang': lang}),
    content_type='application/json'
  )  
  assert response.status_code == status.HTTP_200_OK

def test_get_horoscope_info_with_sign_method_get():
  client = app.test_client()
  response = client.get('/aries/')  
  assert response.status_code == status.HTTP_200_OK

    
# test utils

def test_get_horoscope_info():
  info = horoscope_info(1)      
  assert info is not None

def test_get_horoscope_info_with_date():
  info = horoscope_info(1, '2023-01-01')     
  assert info is not None
  
def test_get_horoscope_info_with_date_and_sign_not_found():
  with pytest.raises(ValueError, match="Sign parameter is required"):    
    horoscope_info(0, '2023-01-01')
  
def test_translate_content_sing():
  content = 'Apr 19, 2023 - Aries, plans to attend a lecture may have to be postponed because someone who\'s going with you feels under the weather. Overindulgence in food or drink may be the reason. This could be something you\'ve wanted to attend for a long time, so make sure you know when and where the event will take place again. Either that or ply your friend with antacids and go anyway!'
  translate = translate_sign(content, 'es')
  assert translate == '19 de abril de 2023 - Aries, los planes para asistir a una conferencia pueden tener que posponerse porque alguien que va contigo se siente bajo el clima.La razón excesiva en la comida o la bebida puede ser la razón.Esto podría ser algo que haya querido asistir durante mucho tiempo, así que asegúrese de saber cuándo y dónde se llevará a cabo el evento nuevamente.¡O eso o conlleva a tu amigo con antiácidos y ve de todos modos!'
  
def test_get_index_from_sign():
  index = get_index_from_sign('aries')
  assert index is not None

def test_get_index_from_sign_and_sign_is_not_found():
  with pytest.raises(ValueError, match="Sign not found in the dictionary of signs."):    
    get_index_from_sign('aries1')
    
    