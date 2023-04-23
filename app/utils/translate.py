from googletrans import Translator, LANGUAGES

NATIVE_LANG = 'en'
translator = Translator(service_urls=['translate.google.com', ])

def is_valid_country_code(country_code: str) -> bool:
  return country_code in LANGUAGES

def text_translate(content: str, target_lang='es') -> str:
  """Translate text to target language."""
  if not content: 
    return ""
  
  if len(content) > 512:
    raise ValueError("Text to translate is too long.")
  
  if not 2 <= len(target_lang) <= 5:
    raise ValueError("Invalid country code.")
       
  if not is_valid_country_code(target_lang):
    raise ValueError("Invalid country code.")
  
  return translator.translate(content, dest=target_lang, src=NATIVE_LANG).text