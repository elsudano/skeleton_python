#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Ventana principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""
import sys
import ttkbootstrap as ttk
from src.config import (ICON_FILE_ICO, ICON_FILE_PNG)

class Window:
    """Clase Ventana.

    Esta clase se encarga de crear la ventana principal de la aplicación.
    """

    __root = None  # Tipo ventana y se crea vacío.
    __height = None
    __width = None
    __title = None

    def __init__(self, title="Información del sistema", width=500, height=500):
        """Create the application's main window.

        Builds the underlying ttkbootstrap.Window with the "superhero"
        theme and the given title/size, and sets its icon.

        Parameters
        ----------
        title : str
            The window title.
        width : int
            The window's width, in pixels.
        height : int
            The window's height, in pixels.
        """
        self.__root = ttk.Window(title=title,themename="superhero",iconphoto=ICON_FILE_PNG,resizable=(True, True),size=(width, height))
        self.__root.iconbitmap(ICON_FILE_ICO)
        self.__height = height
        self.__width = width
        self.__title = title

    def init_ui(self):
        """(Re)apply the window's size, title and position.

        Centers the window on the screen using the currently stored width
        and height, and sets its title and minimum size. Called once the
        view is attached (`View._set_controller`) and again whenever the
        size changes (`set_size`).
        """
        x = (self.__root.winfo_screenwidth() // 2) - (self.__width // 2)
        y = (self.__root.winfo_screenheight() // 2) - (self.__height // 2)
        self.__root.geometry('{}x{}+{}+{}'.format(self.__width, self.__height, x, y))
        self.__root.title(self.__title)
        self.__root.minsize(width=self.__width, height=self.__height)

    def get_theme(self):
        """Return the name of the ttkbootstrap theme currently in use.

        Returns
        -------
        str
            One of 'cosmo', 'flatly', 'darkly', 'superhero', 'solar',
            'cyborg', etc.
        """
        return self.__root.theme_use()

    def set_theme(self, theme):
        """Switch the window to a different ttkbootstrap theme.

        Parameters
        ----------
        theme : str
            One of 'cosmo', 'flatly', 'darkly', 'superhero', 'solar',
            'cyborg', etc.
        """
        self.__root.theme_use(theme)

    def get_size(self):
        """Return the window's currently stored width and height.

        Returns
        -------
        list of int
            A two-item list [width, height].
        """
        return [self.__width,self.__height]

    def set_size(self, width, height):
        """Update the window's stored size and re-apply it.

        Parameters
        ----------
        width : int
            The new width, in pixels.
        height : int
            The new height, in pixels.
        """
        self.__width = width
        self.__height = height
        self.init_ui()

    def change_state_size(self, state):
        """Allow or disallow resizing the window.

        Parameters
        ----------
        state : bool
            True to allow resizing in both directions, False to lock the
            current size.
        """
        self.__root.resizable(width=state, height=state)

    def set_title(self, t):
        """Store a new window title.

        Note: this only updates the stored title; call `init_ui()` (or
        `set_size`, which calls it) to actually apply it to the window.

        Parameters
        ----------
        t : str
            The new window title.
        """
        self.__title = t
        self.init_ui()

    def get(self):
        """Return the underlying ttkbootstrap root window.

        Returns
        -------
        ttkbootstrap.Window
            The root window that every widget in the app is built on.
        """
        return self.__root

    def start(self):
        """Start the Tkinter main event loop.

        Blocks until the window is closed; this is normally the last call
        made in main.py.
        """
        self.__root.mainloop()

    def stop(self):
        """Stop the Tkinter main event loop, closing the window."""
        self.__root.quit()
