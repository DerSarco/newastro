# New Astro API (Because the original one died LOL)
# NOT A SERIOUS DEVELOPMENT

### Spanglish readme
 
Flask API para el curso Intermedio de Android de [Aristidevs](https://github.com/ArisGuimera)


[DEMO](https://newastro.vercel.app/)

# Agradecimientos

 Por dedicarle tiempo a esta basura de proyecto, quiero expresar mis sinceros agradecimientos a:

- [Erix](https://github.com/erix-mx)

Realizamos una petición POST con la siguiente información en formato JSON


# API
```json
{
    "sign":"libra",
    "date":"2020-12-12",
    "lang":"es"
}
```
`URL: https:mi-dominio-horoscope.com/`

Respuesta del servidor:
```json
{
    "icon": "♎",
    "index": 7,
    "content": "19 de abril de 2023 - Este es el día para escuchar y observar, Libra.Hay mucho que aprender de lo que sucede a tu alrededor.Es posible que te sorprenda el impacto de la misma.Demasiadas conversaciones ahora podría resultar infructuosa e incluso volver a ponerlo de alguna manera, especialmente si se usa conversación para ocultar sus inseguridades.Mantenga los ojos y los oídos abiertos.Mañana puedes compartir lo que aprendes."
}
````

Date and Lang se puede omitir de la siguiente manera
```json
{
    "sign":"libra"
}
````

La respuesta debería con la fecha actual y en su idioma general

```json
{
    "icon": "♎",
    "index": 7,
    "content": "Apr 19, 2023 - This is the day to listen and observe, Libra. There is a lot to learn from what's going on around you. You might be surprised at the impact of it. Too much talk now could prove fruitless and even set you back in some way, especially if talk is used to hide your insecurities. Keep your eyes and ears open. Tomorrow you can share what you learn."
}
````

### Método GET
Se envía el signo zodiacal a través del PATH como se muestra a continuación

`URL: https:mi-dominio-horoscope.com/aries`

El resto de parámetros los pasamos por QUERY:

`URL: https:mi-dominio-horoscope.com/aries?date=2022-04-20&lang=es`

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

# Disclaimer

Las respuestas de la API son en el idioma que se cante el orto :)