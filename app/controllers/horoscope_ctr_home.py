from flask import Blueprint, render_template

horoscope_blueprint_home = Blueprint(
  'horoscope_home',
  __name__,
  template_folder='../../templates',
)

@horoscope_blueprint_home.get('/')
def home():    
  return render_template('index.html')

