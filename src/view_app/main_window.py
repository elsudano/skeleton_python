#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Ventana principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""
try:
    import Tkinter as gui_library
except ImportError:
    import tkinter as gui_library


class Window:
    """Clase Ventana.

    Esta clase se encarga de crear la ventana principal de la aplicación.
    """

    __root = None  # Tipo ventana y se crea vacío.
    __height = None
    __width = None
    __title = None

    def __init__(self, title="Información del sistema", width=500, height=500):
        """Constructor por defecto.

        Parameters
        ----------
        title : string
            Este es el título de la ventana.
        width : int
            Indica el tamaño del ancho de la ventana.
        height : int
            Indica el tamaño del alto de la ventana.
        """
        self.__root = gui_library.Tk()
        self.__height = height
        self.__width = width
        self.__title = title

    # def __dark_style(self):
    #     """Estilo de tipo Dark.
    #
    #     Esta función se encarga de formatear todos los componentes para,
    #     simular un entorno dark, en la aplicación.
    #     """
    #     style = ttk.Style()
    #     style.configure("TFrame", background="black")
    #     style.configure("TButton", background="gray")

    def init_ui(self):
        """Inicialización de la ventana.

        Se utilizan parámetros por defecto para crear la ventana principal un,
        tamaño predefinido y un nombre de aplicación y un icono por defecto.
        Como esta función se puede llamar desde cualquier lado para inicializar
        la ventana se pone pública
        """
        x = (self.__root.winfo_screenwidth() // 2) - (self.__width // 2)
        y = (self.__root.winfo_screenheight() // 2) - (self.__height // 2)
        self.__root.geometry('{}x{}+{}+{}'.format(self.__width, self.__height, x, y))
        self.__root.title(self.__title)
        self.__root.minsize(width=self.__width, height=self.__height)

    def size(self, width, height):
        """Asignación del tamaño de la ventana.

        Parameters
        ----------
        width : int
            Indica el tamaño del ancho de la ventana.
        height : int
            Indica el tamaño del alto de la ventana.
        """
        self.__width = width
        self.__height = height
        self.init_ui()

    def change_state_size(self, state):
        """Convierte la ventana para que pueda cambiar de tamaño.

        Parameters
        ----------
        state : boolean
            Indica si se puede maximizar o no la ventana.
        """
        self.__root.resizable(width=state, height=state)

    def set_title(self, t):
        """Asigna el título a la ventana.

        Parameters
        ----------
        t : string
            Especifica el título de la ventana.
        """
        self.__title = t

    def get(self):
        """Devuelve la root de la ventana."""
        return self.__root

    def start(self):
        """Poner en funcionamiento la vista.

        Se utiliza para poder poner el loop proncipal de la aplicación andando.
        """
        self.__root.mainloop()

    def stop(self):
        """Detiene la aplicación.

        Se utiliza para detener la aplicación.
        """
        self.__root.quit()
