#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Lista de controladores del programa.

En este fichero podemos encontrarnos todos los controladores,
de todas las vistas de nuestro programa.
"""

from src.controller.controller import Controller
from src.model.models import *
from src.view_app.views import *


class FirstController(Controller):

    def back(self):
        # FIXME: implementar
        pass

    def change_size(self, event):
        """Cambiar el tamaño de la Ventana
        Con esto hacemos la prueba de como podemos modificar el padre de la vista.
        """
        self._window.size(150, 150)

    def new_view(self, event):
        """Cambia la vista de la ventana.
        Con este método parece que pasamos a otra pantalla de la aplicación.
        """
        model = SecondModel()
        controller = SecondController(self._window, model)
        view = SecondView(self._window, controller)
        view.init_view()

    def test(self, event):
        """Sirve para realizar test en la parte de la GUI"""
        array_of_events = dir(event)
        for pos in range(len(array_of_events)):
            array_of_events[pos] = 'event.' + array_of_events[pos]
            print('Valor de ' + array_of_events[pos] + ' = ')
            print(array_of_events[pos])


class SecondController(Controller):

    def back(self):

        pass
