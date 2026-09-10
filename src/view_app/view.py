#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Clase Base de las vistas del programa.

A partir de esta clase se crearán todas las vistas que tendrá el programa
"""
import tkinter as tk # Tenemos que utilizar tkinter por que ttkbootstrap no tiene los menus
import ttkbootstrap as ttk
from abc import ABC, abstractmethod


class View(ABC):
    """Mainly view Class.
    
    Global Variables:
    ----------------
    _window : Window 
        The Main Window of the app
    _controller : Controller
        The Controller of the View
    _principal_frame : Frame
        The container where we will put all the widgets (Buttons, Labels, etc...)
    _menu_bar : Menu
        The Menu Objet where we will put the Menus
    _menus : list
        This will be the list of the menus that we want to create in our app
    """

    _window = None  # Tipo ventana y se crea vacío.
    _controller = None  # Tipo Controlador y se crea vacío
    _principal_frame = None  # Tipo Frame y se crea vacío, se aloja la parte principal de la ventana
    _menu_bar = None  # Esta es la barra de menus
    _menus = None  # Estos son los menus de la vista
    _tx_logs = None # Esta es la variable para los logs

    @abstractmethod
    def _init_view(self):
        """Build this view's widgets.

        Abstract method that every concrete View must implement to create
        and place its own widgets inside `_principal_frame`.
        """
        pass

    def __init__(self, window):
        """Set up the menu bar and the common widgets shared by every view.

        Builds the base menu (File/Edit/Show/Tools), and creates the shared
        `_principal_frame`, the log panel (`tx_logs`) and the "Exit" button
        that every concrete View reuses; concrete views then add their own
        widgets in `_init_view()`.

        Parameters
        ----------
        window : Window
            The Window where this view will be shown.
        """
        super(View, self).__init__()
        self._window = window
        self._menu_bar = tk.Menu(self._window.get())
        self._menus = list()
        self._window.get().config(menu=self._menu_bar)
        self._add_menu("File")
        self._add_menu("Edit")
        self._add_menu("Show")
        self._add_menu("Tools")
        self._window.set_size(650,400)
        # Creamos el marco
        self._principal_frame = ttk.Frame(self._window.get(), padding="3 3 12 12")
        # El marco está en la posición 0,0 de la ventana en el centro
        self._principal_frame.grid(column=0, row=0, sticky='N'+'S'+'E'+'W')
        # para decirle a la ventana donde esta el grid
        self._window.get().columnconfigure(0, weight=1)
        self._window.get().rowconfigure(0, weight=1)
        # Las columnas y las filas 0 y 12 son fijas y no se mueven 
        # todos los widgets se posicionan entre los números 1 y 11
        # tanto para columnas como para filas
        # cantidad de columnas que tiene el marco
        self._principal_frame.columnconfigure(0, weight=1)
        self._principal_frame.columnconfigure([1,2,3,4,5,6,7,8,9,10,11], weight=1)
        self._principal_frame.columnconfigure(12, weight=0)
        # cantidad de filas que tiene el marco
        self._principal_frame.rowconfigure(0, weight=1)
        self._principal_frame.rowconfigure([1,2,3,4,5,6,7,8,9,10,11], weight=1)
        self._principal_frame.rowconfigure(12, weight=0)
        # Crea el area de logs
        self.l_logs = ttk.Label(self._principal_frame, text="Logs:", bootstyle='secondary')
        self.l_logs.grid(column=1, row=8, sticky='EW')
        self.tx_logs = ttk.ScrolledText(self._principal_frame, width=50, height=5, hbar=True, vbar=True, state='disabled')
        self.tx_logs.grid(column=1, row=9, columnspan=12, sticky='EW')
        # crea botón dentro de marco
        self.b_exit = ttk.Button(self._principal_frame, text="Exit", bootstyle='danger')
        # ponemos en la posición 0,1 y que se expanda a SurEste
        self.b_exit.grid(column=12, row=12, sticky='SE')

    def _append_log(self, message):
        """Append a message to the log panel's text widget.

        Temporarily re-enables the read-only `tx_logs` widget to insert the
        message, scrolls it to the bottom, and disables it again.

        Parameters
        ----------
        message : str
            The message to display in the logs console.
        """
        if self.tx_logs:
            self.tx_logs.config(state='normal')
            self.tx_logs.insert('end', f"{message}\n")
            self.tx_logs.see('end')  # Scroll automático al final
            self.tx_logs.config(state='disabled')

    def _set_controller(self, controller):
        """Attach this view to its controller and finish window initialization.

        Stores the controller reference and calls `Window.init_ui()`, which
        sizes and centers the window now that the view is fully wired up.

        Parameters
        ----------
        controller : Controller
            The controller that will manage this view and its model.
        """
        self._controller = controller
        self._window.init_ui()

    def _add_menu(self, name = ""):
        """Register a new top-level menu in the menu bar.

        Creates the Menu object and appends it to `_menus`; it still needs
        to be attached to the menu bar with `add_cascade` (done once, after
        `_init_view()`, in Controller.__init__).

        Parameters
        ----------
        name : str
            The label of the menu (e.g. "File").
        """
        menu_aux = tk.Menu(self._menu_bar)
        menu_aux.config(title=name)
        # FIXME: arreglar la inclusión de posicionamiento del menú
        # si queremos cambiar para que se pueda añadir un menu en la posición
        # que queremos basta con poner un indice en los parámetros de la
        # función y cambiar el indice por el len de la siguiente linea
        self._menus.insert(len(self._menus), menu_aux)

    def _add_item_menu(self, parent = "", name = "", command = ()):
        """Add a clickable option to one of the registered menus.

        Looks up the menu whose title matches `parent` and appends a new
        command entry to it.

        Parameters
        ----------
        parent : str
            The title of the menu to add the option to (e.g. "File").
        name : str
            The label shown for this menu option.
        command : callable
            The method to run when this menu option is selected.
        """
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

    def _add_menu_separator(self, name = ""):
        """Add a visual separator line to a registered menu.

        Parameters
        ----------
        name : str
            The title of the menu to add the separator to.
        """
        for menu in self._menus:
            if menu.cget('title') == name:
                menu.add_separator()

    def __del__(self):
        """Destroy this view's main frame."""
        self._principal_frame.destroy()
