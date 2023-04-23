from datetime import datetime

import pytest

from app.models.horoscope import Horoscope
from app.repositories.horoscope_repository import HoroscopeRepository
from app.services.horoscope_service import HoroscopeService


def test_get_horoscope_info_with_valid_sign_and_date_and_lang():
    # Arrange
    horoscope_repository = HoroscopeRepository()  
    service = HoroscopeService(horoscope_repository)
    sign = "Aries"
    date = "2023-04-22"
    lang = "es"

    # Act
    result = service.get_horoscope_info(sign, date, lang)

    # Assert
    assert isinstance(result, Horoscope)
    assert result.sign == sign
    assert result.date == date    

def test_get_horoscope_info_with_valid_sign_without_date_and_lang():
    # Arrange
    horoscope_repository = HoroscopeRepository()
    service = HoroscopeService(horoscope_repository)
    sign = "Leo"

    # Act
    result = service.get_horoscope_info(sign)

    # Assert
    assert isinstance(result, Horoscope)
    assert result.sign == sign
    assert result.date == datetime.now().strftime("%Y-%m-%d")  

def test_get_horoscope_info_with_invalid_sign():
    # Arrange
    horoscope_repository = HoroscopeRepository()
    service = HoroscopeService(horoscope_repository)
    sign = "InvalidSign"

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        service.get_horoscope_info(sign)
    assert "Sign not found in the dictionary of signs." in str(excinfo.value)
    
def test_get_horoscope_info_with_invalid_date():
    # Arrange
    horoscope_repository = HoroscopeRepository()
    service = HoroscopeService(horoscope_repository)
    sign = "Virgo"
    date = "invalid_date"

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        service.get_horoscope_info(sign, date)
    assert "time data 'invalid_date'" in str(excinfo.value)
    
def test_get_horoscope_info_with_future_date():
    # Arrange
    horoscope_repository = HoroscopeRepository()
    service = HoroscopeService(horoscope_repository)
    sign = "Sagittarius"
    date = "2030-01-01"

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        service.get_horoscope_info(sign, date)
    assert "Cannot get horoscope for future date" in str(excinfo.value)
    
def test_get_horoscope_info_with_invalid_lang():
    # Arrange
    horoscope_repository = HoroscopeRepository()
    service = HoroscopeService(horoscope_repository)
    sign = "Gemini"
    lang = "invalid_lang"
        
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        service.get_horoscope_info(sign, lang=lang)        
    assert "Invalid country code" in str(excinfo.value)

def test_get_horoscope_info_with_invalid_lang():
    # Arrange
    horoscope_repository = HoroscopeRepository()
    service = HoroscopeService(horoscope_repository)
    sign = "Gemini"
    lang = "invalid_lang"

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        service.get_horoscope_info(sign, lang=lang)
    assert "Invalid country code." in str(excinfo.value)

def test_get_horoscope_info_with_none_date():
    # Arrange
    horoscope_repository = HoroscopeRepository()
    service = HoroscopeService(horoscope_repository)
    sign = "Cancer"

    # Act
    result = service.get_horoscope_info(sign, date=None)

    # Assert
    assert isinstance(result, Horoscope)
    assert result.sign == sign
    assert result.date == datetime.now().strftime("%Y-%m-%d")    

    
    
    