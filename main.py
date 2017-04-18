#!/usr/bin/python
"""Menú principal de la aplicación.

Con este esqueleto se pretende tener un repositorio listo para empezar a,
desarrollar casi caulquier tipo de aplicación con una interfaz miníma.
"""

from src.view_controller.main_controller import Controller
from src.model.main_model import Model

if __name__ == '__main__':
    modelo = Model()
    vista = Controller(500, 500, "Aplicación de Prueba", modelo)
    vista.start()
