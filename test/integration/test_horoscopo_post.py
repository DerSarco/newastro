import json

import pytest
from flask import Flask
from flask.testing import FlaskClient

from app.controllers.horoscope_ctr_post import horoscope_blueprint_post
from app.services.horoscope_service import HoroscopeService
from app.utils.status_code import Status


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(horoscope_blueprint_post)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_post_horoscope(client):
    data = {
        'sign': 'Leo',
        'date': '2023-04-22',
        'lang': 'es'
    }
    response = client.post('/', json=data)    
    assert response.status_code == Status.HTTP_OK
    assert 'horoscope' in json.loads(response.get_data(as_text=True))
    
def test_post_horoscope_when_date_is_future(client):
    data = {
        'sign': 'Leo',
        'date': '2030-04-22'
    }
    response = client.post('/', json=data)
    assert response.status_code == Status.HTTP_BAD_REQUEST 
    assert 'error' in json.loads(response.get_data(as_text=True))   
    
def test_post_horoscope_when_date_is_past(client):
    data = {
        'sign': 'Leo',
        'date': '2010-04-22'
    }
    response = client.post('/', json=data)
    assert response.status_code == Status.HTTP_OK    
    
def test_post_horoscope_when_date_is_invalid(client):
    data = {
        'sign': 'Leo',
        'date': '2010-04-XX'
    }
    response = client.post('/', json=data)
    assert response.status_code == Status.HTTP_BAD_REQUEST
    assert 'error' in json.loads(response.get_data(as_text=True))   
    
def test_post_horoscope_when_lang_is_invalid(client):
    data = {
        'sign': 'Leo',
        'date': '2010-04-22',
        'lang': 'XX'
    }
    response = client.post('/', json=data)
    assert response.status_code == Status.HTTP_BAD_REQUEST
    assert 'error' in json.loads(response.get_data(as_text=True))

def test_post_horoscope_when_sign_is_invalid(client):
    data = {
        'sign': 'XX',
        'date': '2010-04-22'
    }
    response = client.post('/', json=data)
    assert response.status_code == Status.HTTP_BAD_REQUEST
    assert 'error' in json.loads(response.get_data(as_text=True))

def test_post_horoscope_when_sign_is_empty(client):
    data = {
        'date': '2010-04-22'
    }
    response = client.post('/', json=data)        
    assert response.status_code == Status.HTTP_OK        

def test_post_horoscope_when_sign_is_none(client):
    data = {
        'sign': None,
        'date': '2010-04-22'
    }
    response = client.post('/', json=data)    
    assert response.status_code == Status.HTTP_OK










