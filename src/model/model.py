#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Modelo de datos del programa.

Con esto se pretende abstraer toda la logica del programa para que sea mucho,
mas fácil encontrar en donde se encuentra cada parte del programa.
"""

from abc import ABC, abstractmethod


class Model(ABC):
    """Clase controlador."""

    def __init__(self):
        """Constructor por defecto."""
        pass

    @abstractmethod
    def hacer_algo(self):
        pass
