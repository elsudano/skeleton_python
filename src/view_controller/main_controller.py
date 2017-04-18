#!/usr/bin/python
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

import tkinter


class Controller:
    """Clase controlador."""

    __window = None  # Tipo ventana y se crea vacío.
    __height = 500
    __width = 500
    __title = "Título por Defecto"
    __model = None  # Esto almacena la lógica de la aplicación

    def __init__(self, width, height, title, model):
        """Constructor por defecto."""
        self.__window = tkinter.Tk()
        self.__height = height
        self.__width = width
        self.__model = model

    def initialize(self):
        """Inicialización de la ventana.

        Se utilizan parámetros por defecto para crear la ventana proncipal un,
        tamaño predefinido y un nombre de aplicación y un icono por defecto.
        """
        # Aquí es donde tienes que poner la programación para que la ventana se
        # centre en la pantalla.

        self.__window.minsize(width=self.__width, height=self.__height)

    def size(self, width, height):
        """Asignación del tamaño de la ventana."""
        self.__width = width
        self.__height = height

    def start(self):
        """Poner en funcionamiento la vista.

        Se utiliza para poder poner el loop proncipal de la aplicación andando.
        """
        self.initialize()
        self.__window.mainloop()
