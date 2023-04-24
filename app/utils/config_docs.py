from flask import Flask
from flasgger import Swagger

def config_docs(app: Flask):
    swagger = Swagger(
      app,                       
      template={
        "info": {
            "title": "API de Horóscopo",
            "description": "Documentación de la API de Horóscopo",
            "contact": {
                "responsibleOrganization": "",
                "responsibleDeveloper": "",
                "email": "",
                "url": ""
            },
            "version": "0.1"
        },
        "schemes": [            
            "https"
        ],
        "basePath": "/",
        "tags": [
            {
                "name": "Horoscope",
                "description": "Operaciones relacionadas con el horóscopo"
            }
        ],
        "extensions": {
            "x-logo": {
                "url": "https://www.tuorganizacion.com/logo.png",
                "altText": "Logo de Tu Organización"
            }
        }
      }
    )
  