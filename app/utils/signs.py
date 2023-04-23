SIGNS = {
   "aries":{
      "icon":"♈",
      "month":1,
      "name":"Aries"
   },
   "taurus":{
      "icon":"♉",
      "month":2,
      "name":"Taurus",
   },
   "gemini":{
      "icon":"♊",
      "month":3,
      "name":"Gemini"
   },
   "cancer":{
      "icon":"♋",
      "month":4,
      "name":"Cancer"
   },
   "leo":{
      "icon":"♌",
      "month":5,
      "name":"Leo"
   },
   "virgo":{
      "icon":"♍",
      "month":6,
      "name":"Virgo"
   },
   "libra":{
      "icon":"♎",
      "month":7,
      "name":"Libra",
   },
   "scorpio":{
      "icon":"♏",
      "month":8,
      "name":"Scorpion"
   },
   "sagittarius":{
      "icon":"♐",
      "month":9,
      "name":"Sagittarius"
   },
   "capricorn":{
      "icon":"♑",
      "month":10,
      "name":"Capricorn"
   },
   "aquarius":{
      "icon":"♒",
      "month":11,
      "name":"Aquarius"
   },
   "pisces":{
      "icon":"♓",
      "month":12,
      "name":"Pisces"
   }
}

def get_month_from_sign(sign: str) -> int:
        
  if not sign:
    return 1, SIGNS['aries']
  
  sign = sign.lower() 
  if sign in SIGNS:
      index = SIGNS[sign]['month']
      return index, SIGNS[sign]
  raise ValueError("Sign not found in the dictionary of signs.")