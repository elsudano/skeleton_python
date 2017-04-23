#!/usr/bin/python
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""


class Controller:
    """Clase controlador."""

    __model = None  # Esto almacena la lógica de la aplicación

    def __init__(self, model):
        """Constructor por defecto."""
        self.__model = model
