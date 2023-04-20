import json

from flask import Flask, redirect, Response, request, Response
from flask_api import status
from flask import render_template

import os

from api.utils.horoscope_utils import *


app = Flask(__name__, template_folder='templates', static_folder='static',  static_url_path='/static')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.get('/')
def hello_world():
    return render_template('index.html')

@app.post('/')
def horoscope():

    sign = request.json.get('sign', None)
    date = request.json.get('date', None)
    lang = request.json.get('lang', None)
    
    try:        
        sign_object = get_horoscope(sign, date, lang)        
        json_data = json.dumps(sign_object)
        
        return  Response(json_data, status=status.HTTP_200_OK, mimetype='application/json')
    except ValueError as ve:
        return {'message': str(ve)}, status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return {'message': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
    

@app.route('/<sign>/')
def horoscope_get(sign=None):

    date = request.args.get('date', None)
    lang = request.args.get('lang', None)
    
    try:        
        sign_object = get_horoscope(sign, date, lang)        
        json_data = json.dumps(sign_object)
        
        return  Response(json_data, status=status.HTTP_200_OK, mimetype='application/json')
    except ValueError as ve:
        return {'message': str(ve)}, status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return {'message': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
    