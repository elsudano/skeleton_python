#!/usr/bin/python
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

import tkinter


class Controller:
    """Clase controlador."""

    def __init__(self, model):
        """Constructor por defecto."""
        self.__window = tkinter.Tk()
        self.__model = model

    def initialize(self):
        """Inicialización de la ventana.

        Se utilizan parámetros por defecto para crear la ventana proncipal un,
        tamaño predefinido y un nombre de aplicación y un icono por defecto.
        """
        self.__window.minsize(width=260, height=260)

    def go(self):
        """Poner en funcionamiento la vista.

        Se utiliza para poder poner el loop proncipal de la aplicación andando.
        """
        self.__window.mainloop()
