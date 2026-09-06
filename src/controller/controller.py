#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

from abc import ABC, abstractmethod


class Controller(ABC):
    """Clase controlador."""

    _window = None  # Tipo ventana y se crea vacío.
    _model = None  # This save the model of the application
    _view = None  # This save the view of the current application status

    def __init__(self, window, view, model):
        """Constructor por defecto."""
        self._window = window
        self._view = view
        self._model = model
        self._view._set_controller(self)
        # con lo siguiente generamos toda la barra de menus que se ha creado para la vista
        self._view._add_item_menu("File", "New", self.menu_item_new)
        self._view._add_item_menu("File", "Open", self.menu_item_open)
        self._view._add_item_menu("File", "Save", self.menu_item_save)
        self._view._add_item_menu("File", "Exit", self.menu_item_exit)
        self._view._add_item_menu("Edit", "Cut", self.menu_item_cut)
        self._view._add_item_menu("Edit", "Copy", self.menu_item_copy)
        self._view._add_item_menu("Edit", "Paste", self.menu_item_paste)
        self._view._add_item_menu("Show", "Tool Bar", self.menu_item_show_tools_bar)
        self._view._add_item_menu("Show", "Status Bar", self.menu_item_show_status_bar)
        self._view._add_item_menu("Tools", "Utilities", self.menu_item_other)
        self._view._init_view()
        for menu in self._view._menus:
            self._view._menu_bar.add_cascade(label=menu.cget('title'), menu=menu)

    @abstractmethod
    def back(self, event):
        pass

    def change_theme(self):
        """Estilo de tipo Dark.

        Esta función se encarga de formatear todos los componentes para,
        simular un entorno dark, en la aplicación.
        """
        if self._window.get_theme() == "superhero":
            self._window.set_theme("darkly")
        else:
            self._window.set_theme("superhero")

    def menu_item_new(self):
        """Crear un nuevo Objeto.

        Realiza todas las operaciones para crear un nuevo Objeto.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Nuevo
        pass

    def menu_item_open(self):
        """Abrir un Objeto.

        Realiza todas las operaciones para abrir un Objeto.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Abrir
        pass

    def menu_item_save(self):
        """Guardar un Objeto.

        Realiza todas las operaciones para guardar un Objeto.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Guardar
        pass

    def menu_item_cut(self):
        """Corta al portapapeles.

        Lo que hay seleccionado lo pasa al portapapeles para usarlo después, borrando la selección.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Cortar
        pass

    def menu_item_copy(self):
        """Copia al portapapeles.

        Lo que hay seleccionado lo pasa al portapapeles para usarlo después, sin borrar la selección.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Copiar
        pass

    def menu_item_paste(self):
        """Pega el portapapeles.

        Lo que hay en el portapapeles se usa para ponerlo en donde se encuentra el cursor.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Pegar
        pass

    def menu_item_show_tools_bar(self):
        """Mostrar/Ocultar barra de herramientas.

        Con esta opción podemos mostrar u ocultar la barra de herramientas.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Ver/Mostrar barra de herramientas
        pass

    def menu_item_show_status_bar(self):
        """Mostrar/Ocultar barra de estado.

        Con esta opción podemos mostrar u ocultar la barra de estado.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Ver/Mostrar barra de estado
        pass

    def menu_item_other(self):
        """Detener la aplicación.

        Es para detener la aplicación desde el menu Archivo/Salir.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Herramientas/Útiles
        pass

    def menu_item_exit(self):
        """Detener la aplicación.

        Es para detener la aplicación desde el menu Archivo/Salir.
        """
        self.exit_application(None)

    def exit_application(self, event):
        """Detener la aplicación.

        Es para detener la aplicación.
        """
        self._window.stop()