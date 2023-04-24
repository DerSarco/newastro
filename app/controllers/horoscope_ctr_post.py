from flask import Blueprint, jsonify, request

from app.repositories.horoscope_repository import HoroscopeRepository
from app.services.horoscope_service import HoroscopeService
from app.utils.status_code import Status

horoscope_blueprint_post = Blueprint('horoscope_post', __name__)

@horoscope_blueprint_post.route('/', methods=['POST'])
def post_horoscope():
  
  """
  Obtener información del horóscopo
  ---
  tags:
    - Horoscope
  parameters:
    - in: body
      name: body
      schema:
        type: object
        properties:
          sign:
            type: string
            description: Signo del horóscopo
            example: Aries
          date:
            type: string
            description: Fecha del horóscopo
            example: "2020-01-01"
          lang:
            type: string
            description: Idioma del horóscopo
            example: fr
      required: true
  responses:
    200:
      description: Horóscopo obtenido exitosamente
    400:
      description: Error en la solicitud
    500:
      description: Error interno del servidor
  """
  
  sign = request.json.get('sign', None)
  date = request.json.get('date', None)
  lang = request.json.get('lang', None)
  
  horoscope_repository = HoroscopeRepository()
  service = HoroscopeService(horoscope_repository)
  
  try:
    horoscope = service.get_horoscope_info(sign, date, lang)
    url = f"{request.scheme}://{request.host}"
    horoscope.icon = horoscope.icon.format(path=f"{url}/static/assets")
    return jsonify(horoscope.__dict__), Status.HTTP_OK
  except ValueError as e:
    return jsonify({'error': e.args[0]}), Status.HTTP_BAD_REQUEST
  except Exception as e:
    return jsonify({'error': e.args[0]}), Status.HTTP_INTERNAL_SERVER_ERROR
  
  