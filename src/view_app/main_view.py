#!/usr/bin/python
"""Vista principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""
try:
    import Tkinter as gui_library
except ImportError:
    import tkinter as gui_library
from tkinter import ttk


class View:
    """Clase vista."""

    __window = None  # Tipo ventana y se crea vacío.
    __mainframe = None  # Tipo Frame y se crea vacío
    __height = None
    __width = None
    __title = None
    __controller = None  # Esto almacena la lógica de la aplicación

    def __init__(self, controller,
                 title="Información del sistema", width=500, height=500,):
        """Constructor por defecto."""
        self.__window = gui_library.Tk()
        self.__mainframe = ttk.Frame(self.__window, padding="3 3 12 12")
        self.__height = height
        self.__width = width
        self.__title = title
        self.__controller = controller

    def initUI(self):
        """Inicialización de la ventana.

        Se utilizan parámetros por defecto para crear la ventana principal un,
        tamaño predefinido y un nombre de aplicación y un icono por defecto.
        """
        self.__mainframe.grid(column=0, row=0, sticky=('NSEW'))
        self.__mainframe.columnconfigure(0, weight=1)
        self.__mainframe.rowconfigure(0, weight=1)
        x = (self.__window.winfo_screenwidth() // 2) - (self.__width // 2)
        y = (self.__window.winfo_screenheight() // 2) - (self.__height // 2)
        self.__window.geometry('{}x{}+{}+{}'.format(self.__width,
                                                    self.__height, x, y))
        self.__window.title(self.__title)
        self.__window.minsize(width=self.__width, height=self.__height)
        self.__window.resizable(width=False, height=False)

    # def size(self, width, height):
    #     """Asignación del tamaño de la ventana."""
    #     self.__width = width
    #     self.__height = height

    def start(self):
        """Poner en funcionamiento la vista.

        Se utiliza para poder poner el loop proncipal de la aplicación andando.
        """
        self.initUI()
        self.__window.mainloop()
