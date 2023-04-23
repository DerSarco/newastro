import pytest

from app.repositories.horoscope_repository import HoroscopeRepository


class TestHoroscopeRepository:
  
  @pytest.fixture
  def horoscope_repository(self):
    return HoroscopeRepository()
  
  def test_get_horoscope_info_without_date(self, horoscope_repository):
    # Arrange
    sign = 1
    
    # Act
    result = horoscope_repository.get_horoscope_info(sign, None, None)
    
    # Assert
    assert result is not None
    assert isinstance(result, str)
    
  def test_get_horoscope_info_with_date(self, horoscope_repository):
    # Arrange
    sign = 12
    date = "2021-01-01"
    
    # Act
    result = horoscope_repository.get_horoscope_info(sign, date, None)
    
    # Assert
    assert result is not None
    assert isinstance(result, str)
    
  def test_get_horoscope_info_with_invalid_date(self, horoscope_repository):
    # Arrange
    sign = 3
    date = "2021-01-01-01"
    
    # Act & Assert
    with pytest.raises(ValueError):
      horoscope_repository.get_horoscope_info(sign, date, None)  
    
  def test_get_horoscope_info_with_nonexistent_sign(self, horoscope_repository): 
    
    # Arrange
    sign = 13
    
    # Act & Assert
    with pytest.raises(Exception):
      horoscope_repository.get_horoscope_info(sign, None, None)
  
  def test_get_horoscope_info_with_invalid_lang(self, horoscope_repository):
    
    # Arrange
    sign = 4
    lang = "--"
    
    # Act & Assert
    with pytest.raises(Exception):
      horoscope_repository.get_horoscope_info(sign, None, lang)
  
  
    