#!/usr/bin/python
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

    def Frame(self, padre):
        """Modificación de frame."""
        self.__frame = ttk.Frame(padre, padding="3 3 12 12")
