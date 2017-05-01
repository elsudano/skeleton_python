#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

from src.view_app.main_window import Window
from src.view_app.views import FirstView
from src.view_app.views import SecondView
from src.model.main_model import Model


class Controller:
    """Clase controlador."""

    __model = None  # Esto almacena la lógica de la aplicación
    __window = None  # Tipo ventana y se crea vacío.

    def __init__(self):
        """Constructor por defecto."""
        self.__model = Model()
        self.__window = Window("Ventana Principal", 300, 300)
        self.__view = FirstView(self.__window)

    def start_application(self):
        """Ejecutar la aplicación.

        Es para encender la aplicación.
        """
        self.__window.init_ui()
        self.__view.init_view()
        self.__view.b_exit.bind("<Button>", self.exit_application)
        self.__view.b_change_size.bind("<Button>", self.change_size)
        self.__view.b_new_view.bind("<Button>", self.new_view)
        self.__window.start()

    def exit_application(self, event):
        """Detener la aplicación.

        Es para detener la aplicación.
        """
        self.__window.stop()

    def change_size(self, event):
        """Cambiar el tamaño de la Ventana

        Con esto hacemos la prueba de como podemos modificar el padre de la vista.
        """
        self.__window.size(150, 150)

    def new_view(self, event):
        """Cambia la vista de la ventana.

        Con este método parece que pasamos a otra pantalla de la aplicación.
        """
        self.__view.__delete__(self)
        self.__view = SecondView(self.__window)
        self.__view.init_view()
        self.__view.b_exit.bind("<Button>", self.exit_application)
