#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Menú principal de la aplicación.

Con este esqueleto se pretende tener un repositorio listo para empezar a,
desarrollar casi cualquier tipo de aplicación con una interfaz mínima.
"""

import os
from src.config import (ENV_FILE)
from src.view_app.window import Window
from src.model.models import FirstModel
from src.controller.controllers import FirstController
from src.view_app.views import FirstView

if __name__ == '__main__':
    # Creamos la Ventana
    myWindow = Window("Instalación de Aplicación", 650, 400)
    # Creamos el modelo
    myModel = FirstModel()
    # Creamos la vista principal de la aplicación y le añadimos la ventana y el controlador
    myView = FirstView(myWindow)
    # Creamos el controlador de la vista principal y le añadimos la ventana y el modelo
    myController = FirstController(myWindow, myView, myModel)
    # Nos aseguramos que el fichero de credenciales este disponible
    if not os.path.exists(ENV_FILE):
        myModel._log("ADVERTENCIA: No se encontró el archivo .env")
        myModel._log(f"Crea un archivo {ENV_FILE} con tus credenciales.")
        myModel._log("Ejemplo de contenido:")
        myModel._log("YOUTUBE_CLIENT_SECRET_FILE=.credentials/client_secrets.json")
        myModel._log("GMAPS_API_KEY=api_key")
        myModel._log("INSTAGRAM_USERNAME=usuario")
        myModel._log("INSTAGRAM_PASSWORD=password")
    # Hacemos que se muestre la ventana y hacemos funcionar el bucle principal
    myWindow.start()
