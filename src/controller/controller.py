#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

from abc import ABC, abstractmethod


class Controller(ABC):
    """Clase controlador."""

    _window = None  # Tipo ventana y se crea vacío.
    _model = None  # Esto almacena la lógica de la aplicación

    def __init__(self, window, model):
        """Constructor por defecto."""
        self._window = window
        self._model = model

    def exit_application(self, event):
        """Detener la aplicación.

        Es para detener la aplicación.
        """
        self._window.stop()

    @abstractmethod
    def hacer_algo(self):
        pass
