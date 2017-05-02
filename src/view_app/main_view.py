#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Clase Base de las vistas del programa.

A partir de esta clase se crearán todas las vistas que tendnrá el programa 
"""
try:
    from Tkinter import Menu
except ImportError:
    from tkinter import Menu
from abc import ABC, abstractmethod


class View(ABC):
    """Clase Vista Principal."""

    _window = None  # Tipo ventana y se crea vacío.
    _principal_frame = None  # Tipo Frame y se crea vacío, se aloja la parte principal de la ventana
    _menu_bar = None  # Esta es la barra de menus

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
        self._menu_bar = Menu(self._window.get())
        self._window.get().config(menu=self._menu_bar)

    @abstractmethod
    def _init_view(self):
        pass

    def _add_menu(self, name):
        """Añade un menú a la barra de menus"""
        menu_aux = Menu(self._menu_bar)
        self._menu_bar.add_cascade(label=name, menu=menu_aux)

    def _add_item(self, parent, name):
        pass

    def init_view(self):
        """Muestra la vista en la ventana.

        Con este método conseguimos que se muestre la vista en la ventana,
        la cual se le ha pasado por párametros.
        """
        # aquí tienes que mirar el tamaño de la ventana y modificarlo para que se ajuste a la vista
        # self._principal_frame.state()  # cambiar este método por uno que muestre y oculte la vista
        self._init_view()

    def __delete__(self, instance):
        """Con este metodo destruimos el frame principal de la vista."""
        self._principal_frame.destroy()
