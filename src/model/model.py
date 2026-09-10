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
        """Load the .env credentials file, warning if it is missing.

        Every concrete Model shares this constructor: it checks whether the
        .env file referenced by `ENV_FILE` exists and, if not, logs a
        warning explaining how to create it and returns early. If it exists,
        it loads it with python-dotenv so credentials become available via
        `os.getenv`.
        """
        if not os.path.exists(ENV_FILE):
            self._log("ADVERTENCIA: No se encontró el archivo .env")
            self._log(f"Crea un archivo {ENV_FILE} con tus credenciales.")
            self._log("Ejemplo de contenido:")
            self._log("YOUTUBE_CLIENT_SECRET_FILE=.credentials/client_secrets.json")
            self._log("GMAPS_API_KEY=api_key")
            self._log("INSTAGRAM_USERNAME=usuario")
            self._log("INSTAGRAM_PASSWORD=password")
            return
        load_dotenv(ENV_FILE)

    @property
    def log_callback(self):
        """The external observer that receives this Model's log messages.

        IMPORTANT (MVC): the Model must NEVER import or know about the View
        or the Controller - doing so would stop it from being reusable on
        its own (e.g. in tests, in a console script, or behind a different
        interface than this GUI).

        To still be able to report what it is doing, the Model exposes this
        generic "plug" instead (Observer pattern / dependency injection): an
        optional callable that anyone can register from the outside. The
        Model itself does not know or care who is on the other end.

        It is the Controller who, when built (see Controller.__init__ in
        src/controller/controller.py), connects this "plug" to its own
        `graphical_print` method, which is the one that actually knows how
        to get the message to the View. This keeps MVC's dependency
        direction correct: Model <- Controller -> View.

        This is exactly the same pattern already used by ThirdModel's
        `instagram_2fa_callback`, to ask for the Instagram 2FA code through
        the View without importing it directly.

        Returns
        -------
        callable or None
            The registered log callback, or None if nothing has registered
            one yet.
        """
        return getattr(self, '_log_callback', None)

    @log_callback.setter
    def log_callback(self, callback):
        self._log_callback = callback

    def _log(self, message):
        """Notify a log message to whoever is listening.

        If an observer is registered (normally the Controller, through
        `log_callback`), the message is delegated to it and it decides how
        to display it. If none is registered yet - which happens, for
        example, right when the very first Model is built in main.py, before
        any Controller exists to connect it - this falls back to print(), so
        the Model keeps working just as well on its own, without a GUI.

        Parameters
        ----------
        message : str
            The message to log.
        """
        if self.log_callback is not None:
            self.log_callback(message)
        else:
            print(message)

    @abstractmethod
    def hacer_algo(self):
        """Perform this Model's main action.

        Abstract placeholder that every concrete Model must implement.
        """
        pass
