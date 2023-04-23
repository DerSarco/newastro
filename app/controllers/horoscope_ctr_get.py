from flask import Blueprint, jsonify, request

from app.repositories.horoscope_repository import HoroscopeRepository
from app.services.horoscope_service import HoroscopeService
from app.utils.status_code import Status

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
          # Define the properties of the response object here
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
    return jsonify(horoscope.__dict__), Status.HTTP_OK
  except ValueError as e:
    return jsonify({'error': e.args[0]}), Status.HTTP_BAD_REQUEST
  except Exception as e:
    return jsonify({'error': e.args[0]}), Status.HTTP_INTERNAL_SERVER_ERROR
  
  