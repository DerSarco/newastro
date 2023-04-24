# New Astro API (Because the original one died LOL)

![Untitled](README%207caf0ba1a8e04a6e90b903e02563eb91/Untitled.png)

# NOT A SERIOUS DEVELOPMENT (or maybe yes…)

### Spanglish readme

Flask API para el curso Intermedio de Android de [Aristidevs](https://github.com/ArisGuimera/Android-Expert-Intermedio)

[DEMO](https://newastro.vercel.app/)

# Agradecimientos

Por dedicarle tiempo a esta basura de proyecto, quiero expresar mis sinceros agradecimientos a:

- [Erix](https://github.com/erix-mx)

Realizamos una petición POST con la siguiente información en formato JSON

# API

Method POST

```json
{
  "date": "2020-01-01",
  "lang": "fr",
  "sign": "Libra"
}
```

`URL: https://newastro.vercel.app/`

Respuesta del servidor:

```json
{
   "date":"2023-04-23",
   "horoscope":"Apr 23, 2023 - Combine your discipline and expansiveness today and see what manifests. Concentrate on your investments and home. The energy of the day is quite powerful and not something to be taken lightly. You may have much greater control than you realize. Understand that you have to be the one to take the initiative in order to activate the magic of today.",
   "icon":"http://127.0.0.1:5000/static/assets/zodiac-7.png",
   "id":7,
   "sign":"Libra"
}
```

Date and Lang se puede omitir de la siguiente manera

```json
{
  "sign": "Aries"
}
```

La respuesta debería con la fecha actual y en su idioma general

```json
{
   "date":"2023-04-23",
   "horoscope":"Apr 23, 2023 - Do something that inspires the passion within you, Aries. Don't be discouraged by setbacks - be motivated. Use discipline and patience to set your dreams in motion. Be realistic in your approach. The time has come to face the music. Whatever you do, don't shrink into the background and expect others to take care of things for you. The only one who acts in your best interests is you.",
   "icon":"http://127.0.0.1:5000/static/assets/zodiac-1.png",
   "id":1,
   "sign":"Aries"
}
```

### Método GET

Se envía el signo zodiacal a través del PATH como se muestra a continuación

`URL: https://newastro.vercel.app/aries`

El resto de parámetros los pasamos por QUERY:

`URL: https://newastro.vercel.app/aries?date=2022-04-20&lang=es`

Que signos están soportados?

- aries
- taurus
- gemini
- cancer
- leo
- virgo
- libra
- scorpio
- sagittarius
- capricorn
- aquarius
- pisces

## Api docs fue agregado

![Untitled](README%207caf0ba1a8e04a6e90b903e02563eb91/Untitled%201.png)

# Disclaimer

Las respuestas de la API son en el idioma que se te cante el orto 😃, no prometemos traducciones correctas por que google da asco en traducir textos largos. Peace ❤️