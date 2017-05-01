#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Vista principal del programa.

Aqui es donde se pondrán los menus de la aplicación junto con los botones,
necesarios para que funcione la primera vista de la aplicación.
"""
try:
    from Tkinter import ttk
except ImportError:
    from tkinter import ttk
from src.view_app.main_view import View


class FirstView(View):
    """Vista Principal del programa."""

    def _init_view(self):
        """Método de creación de vista.

        En este método es donde realmente se genera la vista de la,
        ventana pues es donde se crean todos los widgets y se colocán,
        en su lugar correspondiente.
        """
        # Creamos el marco
        self._principal_frame = ttk.Frame(self._window.get(), padding="3 3 12 12")
        # El marco está en la posición 0,0 de la ventana en el centro
        self._principal_frame.grid(column=0, row=0, sticky='NSEW')
        # cantidad de columnas que tiene el marco
        self._principal_frame.columnconfigure(0, weight=1)
        # cantidad de filas que tiene el marco
        self._principal_frame.rowconfigure(0, weight=1)
        # crea bóton dentro de marco
        self.b_exit = ttk.Button(self._principal_frame, text="Exit")
        # ponemos en la posición 0,1 y que se expanda a SurEste
        self.b_exit.grid(column=1, row=0, sticky='SE')
        self.b_change_size = ttk.Button(self._principal_frame, text="Change Size")
        self.b_change_size.grid(column=0, row=0, sticky='NW')
        self.b_new_view = ttk.Button(self._principal_frame, text="New View")
        self.b_new_view.grid(column=0, row=1, sticky='S')


class SecondView(View):
    """Vista Principal del programa."""

    def _init_view(self):
        """Método de creación de vista.

        En este método es donde realmente se genera la vista de la,
        ventana pues es donde se crean todos los widgets y se colocán,
        en su lugar correspondiente.
        """
        # Creamos el marco
        self._principal_frame = ttk.Frame(self._window.get(), padding="3 3 12 12")
        # El marco está en la posición 0,0 de la ventana en el centro
        self._principal_frame.grid(column=0, row=0, sticky='NSEW')
        # cantidad de columnas que tiene el marco
        self._principal_frame.columnconfigure(0, weight=1)
        # cantidad de filas que tiene el marco
        self._principal_frame.rowconfigure(0, weight=1)
        # crea bóton dentro de marco
        self.b_exit = ttk.Button(self._principal_frame, text="Exit")
        # ponemos en la posición 0,0 y que se expanda a SurEste
        self.b_exit.grid(column=0, row=0, sticky='SE')