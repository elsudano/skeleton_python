#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Generación fácil de widgets.

Con esta clase se pretende generar los componentes que se pueden ver dentro de,
una ventana de manera sencilla.
"""
try:
    from Tkinter import ttk
except ImportError:
    from tkinter import ttk


class Widgets:
    """Clase Widgets."""

    __button = None
    __checkbutton = None
    __frame = None
    # entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton,
    # scale, Scrollbar, Combobox, Notebook, Progressbar, Separator, Sizegrip,
    # treeview

    def __init__(self):
        """Constructor por defecto."""
        self.__checkbutton = None

    def create_button(self, parent, text, callback):
        """Añade un bóton a la ventana.

        Con esto añadimos un bóton en la ventana en la posición que se,
        indique por el numero que hay en el segundo párametro.
        """
        button = ttk.Button(parent, text=text, command=callback)
        button.grid(row=6, column=6)

    def Frame(self, parent):
        """Modificación de frame."""
        self.__frame = ttk.Frame(parent, padding="3 3 12 12")
