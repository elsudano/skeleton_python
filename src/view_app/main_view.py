#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Clase Base de las vistas del programa.

A partir de esta clase se crearán todas las vistas que tendnrá el programa 
"""

from abc import ABC, abstractmethod


class View(ABC):
    """Clase Vista Principal."""

    _window = None  # Tipo ventana y se crea vacío.
    _principal_frame = None  # Tipo Frame y se crea vacío, se aloja la parte principal de la ventana

    def __init__(self, window):
        """Constructor por defecto.

        Parameters
        ----------
        window : Window
            Esta es una ventana donde se alojarán las diferentes vistas.
        """
        # Esto es para inicializar la Abstract Base Class
        super(View, self).__init__()
        self._window = window

    @abstractmethod
    def _init_view(self):
        pass

    def init_view(self):
        """Muestra la vista en la ventana.

        Con este método conseguimos que se muestre la vista en la ventana,
        la cual se le ha pasado por párametros.
        """
        # aquí tienes que mirar el tamaño de la ventana y modificarlo para que se ajuste a la vista
        # self._principal_frame.state()  # cambiar este método por uno que muestre y oculte la vista
        self._init_view()
