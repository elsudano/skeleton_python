#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Lista de modelos del programa.

En este fichero podemos encontrarnos todos los modelos,
que se pueden usar para nuestro programa.
"""

import os
import simplekml
import instagrapi
import googlemaps
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from src.model.model import Model
from src.config import (CREDENTIALS_DIR,YOUTUBE_CLIENT_SECRET_FILE,YOUTUBE_SESSION_FILE,INSTAGRAM_SESSION_FILE,THUMBNAIL_FILE)

os.makedirs(CREDENTIALS_DIR, exist_ok=True)

class FirstModel(Model):

    def hacer_algo(self):
        """Perform FirstModel's main action.

        FirstModel has no data logic of its own; this is a no-op required
        by the abstract Model interface.
        """
        pass

class SecondModel(Model):

    def hacer_algo(self):
        """Perform SecondModel's main action.

        SecondModel's real logic lives in `get_directions`; this is a no-op
        required by the abstract Model interface.
        """
        pass

    def get_directions(self, from_string, to_string, method, transit_method="rail"):
        """Fetch and log the directions between two stations.

        Queries the Google Maps Directions API for a route between
        `from_string` and `to_string` using the given travel method, and
        logs both the input values and the raw API response. (Building a
        KML file from the transit steps is planned but not implemented yet
        - see the commented-out code below.)

        Parameters
        ----------
        from_string : str
            The name or address of the origin station.
        to_string : str
            The name or address of the destination station.
        method : str
            The Google Maps travel mode ('driving', 'walking', 'bicycling'
            or 'transit').
        transit_method : str, optional
            Reserved for a future transit sub-mode (e.g. 'rail'); currently
            unused. Defaults to 'rail'.
        """
        gmaps = googlemaps.Client(key=os.getenv('GMAPS_API_KEY'))
        directions = None
        if from_string and to_string != "":
            self._log("Values:\n\tFrom:" + from_string + "\n\tTo:" + to_string)
            if method == "transit":
                directions = gmaps.directions(origin=from_string, destination=to_string, mode=method, transit_mode='subway', transit_routing_preference='less_walking')
            else:
                directions = gmaps.directions(origin=from_string, destination=to_string, mode=method)
            self._log(str(directions))
            # kml = simplekml.Kml()
            # for step in directions[0]['legs'][0]['steps']:
            #     if 'transit_details' in step:
            #         print(step)

    # # Configurar API Key de Google Maps
    # gmaps = googlemaps.Client(key='TU_API_KEY')

    # # Obtener ruta con transporte público (incluye metro donde está disponible)
    # directions = gmaps.directions(
    #     "Ikebukuro Station, Tokyo",
    #     "Awajicho Station, Tokyo", 
    #     mode="transit",
    #     transit_mode="subway"
    # )

    # # Convertir a KML automáticamente
    # kml = simplekml.Kml()
    # for step in directions[0]['legs'][0]['steps']:
    #     if 'transit_details' in step:
    #         # Extraer geometría de la ruta de metro
    #         pass

class ThirdModel(Model):

    def hacer_algo(self):
        """Perform ThirdModel's main action.

        ThirdModel's real logic lives in `upload_video`; this is a no-op
        required by the abstract Model interface.
        """
        pass

    def _load_instagram_credentials(self):
        """Load the Instagram username and password from the .env file.

        Returns
        -------
        tuple of (str, str)
            The Instagram username and password.

        Raises
        ------
        Exception
            If either INSTAGRAM_USERNAME or INSTAGRAM_PASSWORD is missing
            from the .env file.
        """
        username = os.getenv('INSTAGRAM_USERNAME')
        password = os.getenv('INSTAGRAM_PASSWORD')
        if not username or not password:
            raise Exception(
                "Credenciales de Instagram no configuradas.\n"
                "Asegúrate de tener un archivo .env con:\n"
                "INSTAGRAM_USERNAME=tu_usuario\n"
                "INSTAGRAM_PASSWORD=tu_contraseña"
            )
        return username, password

    @property
    def instagram_2fa_callback(self):
        """The callback used to ask the user for the Instagram 2FA code.

        Returns
        -------
        callable or None
            The registered callback, or None if none has been registered
            yet (in that case, `_login_con_2fa_instagram` falls back to a
            plain console `input()` prompt).
        """
        return getattr(self, '_instagram_2fa_callback', None)
 
    @instagram_2fa_callback.setter
    def instagram_2fa_callback(self, callback):
        self._instagram_2fa_callback = callback
 
    def _login_con_2fa_instagram(self, client, username, password, max_intentos=3):
        """Log in to Instagram handling the 2FA challenge, with retries.

        Asks for the verification code through `instagram_2fa_callback` (or
        falls back to a console input() prompt if no callback is
        registered) and retries the login up to `max_intentos` times if the
        code is empty or rejected by Instagram.

        Parameters
        ----------
        client : instagrapi.Client
            The Instagram client to log in.
        username : str
            The Instagram username.
        password : str
            The Instagram password.
        max_intentos : int, optional
            Maximum number of attempts before giving up. Defaults to 3.

        Raises
        ------
        Exception
            If no valid code is provided within `max_intentos` attempts.
        """
        for intento in range(1, max_intentos + 1):
            if self.instagram_2fa_callback is not None:
                codigo = self.instagram_2fa_callback()
            else:
                codigo = input("Instagram pide el código de verificación (2FA). Introdúcelo ahora: ")
    
            if not codigo or not codigo.strip():
                if intento == max_intentos:
                    raise Exception("No se ha introducido ningún código de verificación de Instagram.")
                self._log(f"⚠️ Código vacío (intento {intento}/{max_intentos}), inténtalo de nuevo.")
                continue
    
            try:
                client.login(username, password, verification_code=codigo.strip())
                return
            except Exception as e:
                if intento == max_intentos:
                    raise Exception(f"Código 2FA incorrecto tras {max_intentos} intentos: {e}")
                self._log(f"⚠️ Código incorrecto (intento {intento}/{max_intentos}), inténtalo de nuevo.")

    def _get_instagram_client(self):
        """Return an authenticated instagrapi Client, reusing a saved session.

        Tries to reuse the session stored in INSTAGRAM_SESSION_FILE first;
        if it is missing or no longer valid, performs a full login instead
        (asking for the 2FA code through the registered callback when
        Instagram requires it) and saves the new session for next time.

        Returns
        -------
        instagrapi.Client
            An authenticated Instagram client.
        """
        username, password = self._load_instagram_credentials()
        client = instagrapi.Client()
        login_via_session = False
        if os.path.exists(INSTAGRAM_SESSION_FILE):
            try:
                session = client.load_settings(INSTAGRAM_SESSION_FILE)
                client.set_settings(session)
                client.login(username, password)
                client.get_timeline_feed()
                login_via_session = True
                self._log("Instagram: sesión reutilizada (sin pedir 2FA).")
            except Exception as e:
                self._log(f"Instagram: la sesión guardada ya no es válida ({e}). Se requiere login completo.")
                login_via_session = False
        if not login_via_session:
            client = instagrapi.Client()
            try:
                client.login(username, password)
            except instagrapi.exceptions.TwoFactorRequired:
                self._login_con_2fa_instagram(client, username, password)
            except Exception as e:
                if "two-factor" in str(e).lower() or "2fa" in str(e).lower():
                    self._login_con_2fa_instagram(client, username, password)
                else:
                    raise
            client.dump_settings(INSTAGRAM_SESSION_FILE)
            self._log("Instagram: login completo y sesión guardada para la próxima vez.")
        return client

    def _upload_to_youtube(self, string_path, string_title, text_description):
        """Upload a video to YouTube using the YouTube Data API.

        Reuses saved OAuth credentials from YOUTUBE_SESSION_FILE when
        available and valid (refreshing them if expired), or otherwise runs
        the OAuth flow via a local server and saves the resulting
        credentials for next time. Uploads the video as a public, resumable
        upload.

        Parameters
        ----------
        string_path : str
            Path to the video file to upload.
        string_title : str
            Title for the YouTube video.
        text_description : str
            Description for the YouTube video.
        """
        creds = None
        # Cargar credenciales guardadas
        if os.path.exists(YOUTUBE_SESSION_FILE):
            creds = Credentials.from_authorized_user_file(YOUTUBE_SESSION_FILE)
        # Si no hay credenciales válidas, iniciar flujo OAuth
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(YOUTUBE_CLIENT_SECRET_FILE,scopes=['https://www.googleapis.com/auth/youtube.upload'])
                creds = flow.run_local_server(port=0)
            # Guardar credenciales para futuras ejecuciones
            with open(YOUTUBE_SESSION_FILE, 'w') as token:
                token.write(creds.to_json())
        # 2. Construir el servicio de YouTube
        youtube = build('youtube', 'v3', credentials=creds)
        # 3. Preparar metadatos
        body = {'snippet': {'title': string_title,'description': text_description,'categoryId': '22'},'status': {'privacyStatus': 'public'} # 'private' para pruebas, cambiar a 'public' cuando esté listo
        }
        # 4. Preparar y subir el video
        media = MediaFileUpload(string_path, resumable=True)
        request = youtube.videos().insert(part='snippet,status',body=body,media_body=media)
        # 5. Ejecutar la subida
        response = request.execute()

    def _upload_to_instagram(self, string_path, string_title, text_description):
        """Upload a video to Instagram as a Reel using instagrapi.

        Translates the most common instagrapi failure modes (file too
        large, unsupported format, rate limiting, expired session) into
        clearer Exception messages for the caller.

        Parameters
        ----------
        string_path : str
            Path to the video file to upload.
        string_title : str
            Used as the first line of the Instagram caption.
        text_description : str
            Used as the rest of the Instagram caption, after the title.

        Raises
        ------
        Exception
            With a user-friendly message describing what went wrong.
        """
        try:
            # Inicializar el cliente de Instagram
            client = self._get_instagram_client()
            # Subir el video
            result = client.clip_upload(string_path,caption=f"{string_title}\n\n{text_description}",thumbnail=THUMBNAIL_FILE,)
            self._log(f"Instagram subido. ID: {result.id}")
        except instagrapi.exceptions.LoginRequired:
            raise Exception("La sesión de Instagram ha expirado. Verifica tus credenciales.")
        except instagrapi.exceptions.ClientError as e:
            if "media is too large" in str(e).lower():
                raise Exception("El archivo es demasiado grande para Instagram (máx. 100MB).")
            elif "unsupported media" in str(e).lower():
                raise Exception("Formato de video no soportado por Instagram.")
            elif "too many requests" in str(e).lower():
                raise Exception("Demasiadas peticiones a Instagram. Espera unos minutos.")
            else:
                raise Exception(f"Error de Instagram: {str(e)}")
        except Exception as e:
            raise Exception(f"Error inesperado en Instagram: {str(e)}")

    def upload_video(self, string_path, string_title, string_location, text_description, cb_platforms):
        """Upload a video to the selected platforms and collect the results.

        Logs the received values for review, then attempts the upload on
        each platform requested in `cb_platforms` (YouTube and/or
        Instagram), catching and logging any errors per platform instead of
        stopping at the first failure.

        Note: `string_location` is currently only logged, it is not actually
        sent to either platform yet.

        Parameters
        ----------
        string_path : str
            Path to the video file to upload.
        string_title : str
            Title/caption text used for the upload.
        string_location : str
            Geolocation text (currently not sent to either platform).
        text_description : str
            Description/caption text used for the upload.
        cb_platforms : list of str
            Which platforms to upload to; any combination of 'youtube' and
            'instagram'.

        Returns
        -------
        dict
            A dict with 'exitosas' (list of platform names that succeeded),
            'fallidas' (list of platform names that failed) and 'errores'
            (dict mapping platform name to its error message).
        """
        # Variable para recoger los datos
        resultados = {'exitosas': [],'fallidas': [],'errores': {}}
        # 0. Verificamos visualmente que todos los datos son correctos
        self._log('Valor de Path:' + string_path)
        self._log('Valor de Título:' + string_title)
        self._log('Valor de GeoLocalización:' + string_location)
        self._log('Valor de Plataformas: ' + str(cb_platforms))
        self._log('Valor de Descripción:\n' + text_description)

        if "youtube" in cb_platforms:
            try:
                self._log("📤 Subiendo a YOUTUBE...")
                self._upload_to_youtube(string_path, string_title, text_description)
                resultados['exitosas'].append('YouTube')
                self._log("✅ YouTube: Subida exitosa")
            except Exception as e:
                error_msg = str(e)
                resultados['fallidas'].append('YouTube')
                resultados['errores']['YouTube'] = error_msg
                self._log(f"❌ YouTube: Error - {error_msg}")
        if "instagram" in cb_platforms:
            try:
                self._log("📤 Subiendo a INSTAGRAM...")
                self._upload_to_instagram(string_path, string_title, text_description)
                resultados['exitosas'].append('Instagram')
                self._log("✅ Instagram: Subida exitosa")
            except instagrapi.exceptions.LoginRequired:
                error_msg = "La sesión de Instagram ha expirado. Vuelve a iniciar sesión."
                resultados['fallidas'].append('Instagram')
                resultados['errores']['Instagram'] = error_msg
                self._log(f"❌ Instagram: Error - {error_msg}")
            except instagrapi.exceptions.ClientError as e:
                error_msg = f"Error del cliente de Instagram: {str(e)}"
                resultados['fallidas'].append('Instagram')
                resultados['errores']['Instagram'] = error_msg
                self._log(f"❌ Instagram: Error - {error_msg}")
            except Exception as e:
                error_msg = f"Error inesperado en Instagram: {str(e)}"
                resultados['fallidas'].append('Instagram')
                resultados['errores']['Instagram'] = error_msg
                self._log(f"❌ Instagram: Error - {error_msg}")
        return resultados
