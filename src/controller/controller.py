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
    _model = None  # Esto almacena la lógica de la aplicación

    def __init__(self, window, model):
        """Constructor por defecto."""
        self._window = window
        self._model = model

    @abstractmethod
    def back(self):
        pass

    def menu_item_new(self):
        """Crear un nuevo Objeto.

        Realiza todas las operaciones para crear un nuevo Objeto.
        """
        # FIXME: implementar Archivo/Nuevo
        pass

    def menu_item_open(self):
        """Abrir un Objeto.

        Realiza todas las operaciones para abrir un Objeto.
        """
        # FIXME: implementar Archivo/Abrir
        pass

    def menu_item_save(self):
        """Guardar un Objeto.

        Realiza todas las operaciones para guardar un Objeto.
        """
        # FIXME: implementar Archivo/Guardar
        pass

    def menu_item_cut(self):
        """Corta al portapapeles.

        Lo que hay seleccionado lo pasa al portapapeles para usarlo despúes, borrando la selección.
        """
        # FIXME: implementar Editar/Cortar
        pass

    def menu_item_copy(self):
        """Copia al portapapeles.

        Lo que hay seleccionado lo pasa al portapapeles para usarlo despúes, sin borrar la selección.
        """
        # FIXME: implementar Editar/Copiar
        pass

    def menu_item_paste(self):
        """Pega el portapapeles.

        Lo que hay en el portapapeles se usa para ponerlo en donde se encuentra el cursor.
        """
        # FIXME: implementar Editar/Pegar
        pass

    def menu_item_show_tools_bar(self):
        """Mostrar/Ocultar barra de herramientas.

        Con esta opción podemos mostrar u ocultar la barra de herramientas.
        """
        # FIXME: implementar Ver/Mostrar barra de herramientas
        pass

    def menu_item_show_status_bar(self):
        """Mostrar/Ocultar barra de estado.

        Con esta opción podemos mostrar u ocultar la barra de estado.
        """
        # FIXME: implementar Ver/Mostrar barra de estado
        pass

    def menu_item_other(self):
        """Detener la aplicación.

        Es para detener la aplicación desde el menu Archivo/Salir.
        """
        # FIXME: implementar Herramientas/Utiles
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