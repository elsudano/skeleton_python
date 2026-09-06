#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Clase Base de las vistas del programa.

A partir de esta clase se crearán todas las vistas que tendrá el programa
"""
import tkinter as tk # Tenemos que utilizar tkinter por que ttkbootstrap no tiene los menus
from abc import ABC, abstractmethod


class View(ABC):
    """Clase Vista Principal."""

    _window = None  # Tipo ventana y se crea vacío.
    _controller = None  # Tipo Controlador y se crea vacío
    _principal_frame = None  # Tipo Frame y se crea vacío, se aloja la parte principal de la ventana
    _menu_bar = None  # Esta es la barra de menus
    _menus = None  # Estos son los menus de la vista

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
        self._menu_bar = tk.Menu(self._window.get())
        self._menus = list()
        self._window.get().config(menu=self._menu_bar)
        self._add_menu("File")
        self._add_menu_separator("File")
        self._add_menu("Edit")
        self._add_menu("Show")
        self._add_menu("Tools")
 
    def _set_controller(self, controller):
        """Setting the controller of the view.
        Parameters
        ----------
        controller : Controller
            This will be the controller that manage the view and the model that we will use to the application
        """
        self._controller = controller
        self._add_item_menu("Tools", "Change Theme", self._controller.change_theme)
        self._window.init_ui()

    @abstractmethod
    def _init_view(self):
        pass

    def _add_menu(self, name):
        """Añade un menú a la barra de menus"""
        menu_aux = tk.Menu(self._menu_bar)
        menu_aux.config(title=name)
        # FIXME: arreglar la inclusión de posicionamiento del menú
        # si queremos cambiar para que se pueda añadir un menu en la posición
        # que queremos basta con poner un indice en los parámetros de la
        # función y cambiar el indice por el len de la siguiente linea
        self._menus.insert(len(self._menus), menu_aux)

    def _add_item_menu(self, parent, name, command):
        """Añade una opción a los menus"""
        for menu in self._menus:
            if menu.cget('title') == parent:
                menu.add_command(label=name, command=command)
                # menu.add_command(label=name)
                # FIXME: arreglar la inclusión de posicionamiento del item del menú
                # menu.insert_command(0, label=name, command=command)
                # si queremos cambiar para que se pueda añadir una opción de menu
                # en la posición que queremos basta con poner un indice en los
                # parámetros de la función y cambiar el indice de la función anterior
                # por el que se pasa por parámetros.

    def _add_menu_separator(self, name):
        """Añade un separador al menu"""
        for menu in self._menus:
            if menu.cget('title') == name:
                menu.add_separator()

    def __delete__(self, instance):
        """Con este método destruimos el frame principal de la vista."""
        self._principal_frame.destroy()
