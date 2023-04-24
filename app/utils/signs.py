SIGNS = {
   "aries":{
      "icon":"{path}/zodiac-1.png",
      "id":1,
      "name":"Aries"
   },
   "taurus":{
      "icon":"{path}/zodiac-2.png",
      "id":2,
      "name":"Taurus",
   },
   "gemini":{
      "icon":"{path}/zodiac-3.png",
      "id":3,
      "name":"Gemini"
   },
   "cancer":{
      "icon":"{path}/zodiac-4.png",
      "id":4,
      "name":"Cancer"
   },
   "leo":{
      "icon":"{path}/zodiac-5.png",
      "id":5,
      "name":"Leo"
   },
   "virgo":{
      "icon":"{path}/zodiac-6.png",
      "id":6,
      "name":"Virgo"
   },
   "libra":{
      "icon":"{path}/zodiac-7.png",
      "id":7,
      "name":"Libra",
   },
   "scorpio":{
      "icon":"{path}/zodiac-8.png",
      "id":8,
      "name":"Scorpion"
   },
   "sagittarius":{
      "icon":"{path}/zodiac-9.png",
      "id":9,
      "name":"Sagittarius"
   },
   "capricorn":{
      "icon":"{path}/zodiac-10.png",
      "id":10,
      "name":"Capricorn"
   },
   "aquarius":{
      "icon":"{path}/zodiac-11.png",
      "id":11,
      "name":"Aquarius"
   },
   "pisces":{
      "icon":"{path}/zodiac-12.png",
      "id":12,
      "name":"Pisces"
   }
}

def get_id_from_sign(sign: str) -> int:
        
  if not sign:
    return 1, SIGNS['aries']
  
  sign = sign.lower() 
  if sign in SIGNS:
      index = SIGNS[sign]['id']
      return index, SIGNS[sign]
  raise ValueError("Sign not found in the dictionary of signs.")