import pytest
from app.utils.signs import SIGNS, get_month_from_sign

def test_get_month_from_sign_valid_sign():    
    
    # Arrange
    sign = 'leo'
    expected_month = 5
    expected_result = (expected_month, SIGNS[sign])    
    # Assert
    assert get_month_from_sign(sign) == expected_result

def test_get_month_from_sign_empty_sign():
    # Arrange
    sign = ''
    expected_month = 1
    expected_result = (expected_month, SIGNS['aries'])    
    # Assert
    assert get_month_from_sign(sign) == expected_result

def test_get_month_from_sign_invalid_sign():
    # Arrange
    sign = 'invalid_sign'
    
    # Assert
    with pytest.raises(ValueError):
        get_month_from_sign(sign)