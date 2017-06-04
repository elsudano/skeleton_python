#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Menú principal de la aplicación.

Con este esqueleto se pretende tener un repositorio listo para empezar a,
desarrollar casi cualquier tipo de aplicación con una interfaz miníma.
"""
from src.view_app.window import Window
from src.model.models import FirstModel
from src.controller.controllers import FirstController
from src.view_app.views import FirstView


if __name__ == '__main__':
    # Creamos la Ventana
    myWindow = Window("Instalación de Aplicación", 600, 350)
    # Creamos el modelo
    myModel = FirstModel()
    # Creamos el controlador de la vista principal y le añadimos la ventana y el modelo
    myController = FirstController(myWindow, myModel)
    # Creamos la vista principal de la aplicación y le añadimos la ventana y el controlador
    myView = FirstView(myWindow, myController)
    # inicializamos la vista principal
    myView.init_view()
    # Hacemos que se muestre la ventana y hacemos funcionar el bucle principal
    myWindow.start()
