import json

import pytest
from flask import Flask

from app.controllers.horoscope_ctr_home import horoscope_blueprint_home
from app.services.horoscope_service import HoroscopeService
from app.utils.status_code import Status


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(horoscope_blueprint_home)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_horoscope_working(client):    
    response = client.get('/')        
    assert response.status_code == Status.HTTP_OK    
    

