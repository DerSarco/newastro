from app.utils.translate import text_translate
import pytest

def test_text_translate_valid_country_code():
    content = "Hello"
    target_lang = "es"
    translated_text = text_translate(content, target_lang)
    assert isinstance(translated_text, str)
    assert len(translated_text) > 0

def test_text_translate_invalid_country_code():
    content = "Hello"
    target_lang = "invalid_code"
    with pytest.raises(ValueError):
        text_translate(content, target_lang)
        
def test_text_translate_empty_content():
    content = ""
    target_lang = "es"
    translated_text = text_translate(content, target_lang)
    assert isinstance(translated_text, str)
    assert len(translated_text) == 0        

def test_text_translate_valid_input():    
    # Valid input
    content = "Hello"
    target_lang = 'es'
    translated_text = text_translate(content, target_lang)
    assert isinstance(translated_text, str)
    assert translated_text != ""        
        
def test_text_translate_empty_input():
    # Empty input
    content = ""
    target_lang = 'es'
    translated_text = text_translate(content, target_lang)
    assert isinstance(translated_text, str)
    assert translated_text == ""
        
def test_text_translate_long_text():
    # Text too long
    content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel ullamcorper elit. Quisque sit amet feugiat mi, non fermentum erat. Vestibulum sodales ultrices nisl, in tempor sapien. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel ullamcorper elit. Quisque sit amet feugiat mi, non fermentum erat. Vestibulum sodales ultrices nisl, in tempor sapien. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel ullamcorper elit. Quisque sit amet feugiat mi, non fermentum erat. Vestibulum sodales ultrices nisl, in tempor sapien. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel ullamcorper elit. Quisque sit amet feugiat mi, non fermentum erat. Vestibulum sodales ultrices nisl, in tempor sapien."
    target_lang = 'es'
    with pytest.raises(ValueError) as e:
        text_translate(content, target_lang)
    assert "Text to translate is too long." in str(e.value)

def test_text_translate_invalid_country_code():
    # country code invalid 
    content = "Hello"
    target_lang = 'invalid_code'
    with pytest.raises(ValueError) as e:
        text_translate(content, target_lang)
    assert "Invalid country code." in str(e.value)

def test_text_translate_short_country_code():
    # country code too short
    content = "Hello"
    target_lang = 'e'
    with pytest.raises(ValueError) as e:
        text_translate(content, target_lang)
    assert "Invalid country code." in str(e.value)

def test_text_translate_long_country_code():
    # country code too long
    content = "Hello"
    target_lang = 'invalid_long_code'
    with pytest.raises(ValueError) as e:
        text_translate(content, target_lang)
    assert "Invalid country code." in str(e.value)        
        
        
        