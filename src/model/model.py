#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Modelo de datos del programa.

Con esto se pretende abstraer toda la lógica del programa para que sea mucho,
mas fácil encontrar en donde se encuentra cada parte del programa.
"""

import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from src.config import ENV_FILE

class Model(ABC):
    """Clase controlador."""

    def __init__(self):
        """Constructor por defecto."""
        if not os.path.exists(ENV_FILE):
            print("ADVERTENCIA: No se encontró el archivo .env")
            print(f"Crea un archivo {ENV_FILE} con tus credenciales.")
            print("Ejemplo de contenido:")
            print("YOUTUBE_CLIENT_SECRET_FILE=.credentials/client_secrets.json")
            print("INSTAGRAM_USERNAME=usuario")
            print("INSTAGRAM_PASSWORD=password")
            return
        load_dotenv(ENV_FILE)

    @abstractmethod
    def hacer_algo(self):
        pass
