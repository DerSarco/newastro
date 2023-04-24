from flask import Flask

from app.controllers.horoscope_ctr_get import horoscope_blueprint_get
from app.controllers.horoscope_ctr_home import horoscope_blueprint_home
from app.controllers.horoscope_ctr_post import horoscope_blueprint_post
from app.utils.config_docs import config_docs


def create_app():
    
    app = Flask(__name__, static_folder='../static', static_url_path='/static')  
    
    # Register blueprints
    app.register_blueprint(horoscope_blueprint_post)
    app.register_blueprint(horoscope_blueprint_get)
    app.register_blueprint(horoscope_blueprint_home)
    
    config_docs(app)
    
    return app