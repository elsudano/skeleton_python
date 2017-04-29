#!/usr/bin/python
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

from src.view_app.main_window import Window
from src.view_app.main_view import View
from src.model.main_model import Model


class Controller:
    """Clase controlador."""

    __model = None  # Esto almacena la lógica de la aplicación
    __window = None  # Tipo ventana y se crea vacío.

    def __init__(self):
        """Constructor por defecto."""
        self.__model = Model()
        self.__window = Window("Prueba", 400, 500)
        self.__view = View(self.__window)
        self.__view.show()
        self.__view.__mainframe.b.bind("<Button>", self.exit_application)
        # self.__view.c.bind("<Button>", self.exit_application)

    def start_application(self):
        """Ejecutar la aplicación.

        Es para encender la aplicación.
        """
        self.__window.start()

    def exit_application(self):
        """Detener la aplicación.

        Es para detener la aplicación.
        """
        exit()
