#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

from src.view_app.main_window import Window
from src.view_app.first_view import FirstView
from src.model.main_model import Model


class Controller:
    """Clase controlador."""

    __model = None  # Esto almacena la lógica de la aplicación
    __window = None  # Tipo ventana y se crea vacío.

    def __init__(self):
        """Constructor por defecto."""
        self.__model = Model()
        self.__window = Window("Prueba", 400, 500)
        self.__view = FirstView(self.__window)

    def m_start_application(self):
        """Ejecutar la aplicación.

        Es para encender la aplicación.
        """
        self.__window.init_ui()
        self.__view.init_view()
        self.__view.b_exit.bind("<Button>", self.m_exit_application)
        self.__view.b_change_size.bind("<Button>", self.m_change_size)
        self.__window.start()

    def m_exit_application(self, event):
        """Detener la aplicación.

        Es para detener la aplicación.
        """
        self.__window.stop()

    def m_change_size(self, event):
        """Cambiar el tamaño de la Ventana

        Con esto hacemos la prueba de como podemos modificar el padre de la vista.
        """
        self.__window.size(300, 300)
