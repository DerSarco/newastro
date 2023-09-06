from flask import Blueprint, jsonify, request

from app.repositories.horoscope_repository import HoroscopeRepository
from app.services.horoscope_service import HoroscopeService
from app.utils.status_code import Status
from app.utils.signs import SIGNS

horoscope_blueprint_get = Blueprint('horoscope_get', __name__)


@horoscope_blueprint_get.route('/<sign>/', methods=['GET'])
def get_horoscope(sign=None):
  
  """
  Get horoscope information for a specific sign.

  ---
  tags:
    - Horoscope
  parameters:
    - name: sign
      in: path
      type: string
      required: true
      description: Zodiac sign for which to retrieve the horoscope information.
    - name: date
      in: query
      type: string
      description: Date for which to retrieve the horoscope information. format "YYYY-MM-DD"
    - name: lang
      in: query
      type: string
      description: Language of the horoscope information to retrieve.
  responses:
    200:
      description: OK
      schema:
        type: object
        properties:
          sign:
            type: string
            description: Signo
            example: aries
          date:
            type: string
            description: fecha del horoscopo
            example: "2020-01-01"
          horoscope:
            type: string
            description: Horoscopo del signo
            example: Hoy será un día asqueroso para ti.
          icon:
            type: string
            description: imagen del signo
            example: ...assets/img/horoscope/aries.png
          id:
            type: id
            description: id del signo
            example: 10
    400:
      description: Bad Request
      schema:
        type: object
        properties:
          error:
            type: string
            description: Error message describing the bad request.
    500:
      description: Internal Server Error
      schema:
        type: object
        properties:
          error:
            type: string
            description: Error message describing the internal server error.
  """
  
  date = request.args.get('date', None)
  lang = request.args.get('lang', None)
  
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
  
@horoscope_blueprint_get.route('/list/', methods=['GET'])
def get_horoscope_list():
  """
  Obtener la lista de horóscopos.

  Devuelve la lista de horóscopos con sus iconos y URLs de imágenes actualizadas.

  ---
  tags:
    - Horoscope  
  responses:
    200:
      description: Lista de horóscopos con iconos y URLs de imágenes actualizadas
      schema:
        type: array
        items:
          type: object
          properties:
            icon:
              type: string
              description: Icono del horóscopo
              example: ...assets/img/horoscope/aries.png
            id:
              type: integer
              description: ID del horóscopo
              example: 1
            name:
              type: string
              description: Nombre del horóscopo
              example: Aries

  """
  url = f"{request.scheme}://{request.host}"
  list_sign = list(map(lambda sign: {**sign, "icon": sign["icon"].format(path=f"{url}/static/assets")}, SIGNS.values()))
  return jsonify(list_sign), Status.HTTP_OK