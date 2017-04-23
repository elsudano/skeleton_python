#!/usr/bin/python
"""Menú principal de la aplicación.

Con este esqueleto se pretende tener un repositorio listo para empezar a,
desarrollar casi caulquier tipo de aplicación con una interfaz miníma.
"""

from src.model.main_model import Model
from src.controller.main_controller import Controller
from src.view_app.main_view import View

if __name__ == '__main__':
    modelo = Model()
    controlador = Controller(modelo)
    vista = View(controlador, "Aplicación de Prueba", 500, 500)
    vista.start()
