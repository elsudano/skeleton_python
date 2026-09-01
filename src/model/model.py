#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Modelo de datos del programa.

Con esto se pretende abstraer toda la lógica del programa para que sea mucho,
mas fácil encontrar en donde se encuentra cada parte del programa.
"""

import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv

class Model(ABC):
    """Clase controlador."""

    def __init__(self):
        """Constructor por defecto."""
        env_file = '.env'
        if not os.path.exists(env_file):
            print("ADVERTENCIA: No se encontró el archivo .env")
            print(f"Crea un archivo {env_file} con tus credenciales.")
            print("Ejemplo de contenido:")
            print("INSTAGRAM_USERNAME=tu_usuario")
            print("INSTAGRAM_PASSWORD=tu_contraseña")
            return
        load_dotenv()

    @abstractmethod
    def hacer_algo(self):
        pass
