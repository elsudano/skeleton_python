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


class View:
    """Clase Vista Principal.

    Esta clase se encarga de crear los botones y demas widgets,
    para el menú principal de la aplicación.
    """

    __window = None  # Tipo ventana y se crea vacío.
    __mainframe = None  # Tipo Frame y se crea vacío

    def __init__(self, window,):
        """Constructor por defecto.

        Parameters
        ----------
        window : Window
            Esta es una ventana donde se alojarán las diferentes vistas.
        """
        self.__window = window

    def __initVIEW(self):
        """Método de creación de vista.

        En este método es donde realmente se genera la vista de la,
        ventana pues es donde se crean todos los widgets y se colocán,
        en su lugar correspondiente.
        """
        # Creamos el marco
        self.__mainframe = ttk.Frame(self.__window.get(), padding="3 3 12 12")
        # El marco está en la posición 0,0 de la ventana en el centro
        self.__mainframe.grid(column=0, row=0, sticky=('NSEW'))
        # cantidad de columnas que tiene el marco
        self.__mainframe.columnconfigure(12, weight=1)
        # cantidad de filas que tiene el marco
        self.__mainframe.rowconfigure(12, weight=1)
        # crea bóton dentro de marco
        b = ttk.Button(self.__mainframe, text="Salir")
        # ponemos en la posición 6,6 y que se expanda a SurEste
        b.grid(column=6, row=6, sticky=('SE'))
        c = ttk.Button(self.__mainframe, text="Prueba")
        c.grid(column=0, row=0, sticky=('NW'))

#    def get_view(self):
#        """Devuelve la vista."""
#        return self.__mainframe

    def show(self):
        """Muestra la vista en la ventana.

        Con este método conseguimos que se muestre la vista en la ventana,
        la cual se le ha pasado por párametros.
        """
        self.__initVIEW()
        self.__mainframe.state()  # cambiar este método por uno que
        # muestre y oculte la vista
