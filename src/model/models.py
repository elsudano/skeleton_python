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

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_CREDENTIALS_DIR = os.path.join(_PROJECT_ROOT, '.credentials')
os.makedirs(_CREDENTIALS_DIR, exist_ok=True)
 
INSTAGRAM_SESSION_FILE = os.path.join(_CREDENTIALS_DIR, 'instagram_session.json')
YOUTUBE_SESSION_FLE = os.path.join(_CREDENTIALS_DIR, 'youtube_session.json')

class FirstModel(Model):

    def hacer_algo(self):
        pass

class SecondModel(Model):

    def hacer_algo(self):
        pass

    def get_directions(self, from_string, to_string, method, transit_method="rail"):
        """With this app we can create a KML file with the route from Google Maps"""
        gmaps = googlemaps.Client(key='AIzaSyC-HHbRpdeiw2Q1ZsIJ3Cgg8MEAZPBuPAI')
        directions = None
        if from_string and to_string != "":
            print("Values:\n\tFrom:" + from_string + "\n\tTo:" + to_string)
            if method == "transit":
                directions = gmaps.directions(origin=from_string, destination=to_string, mode=method, transit_mode='subway', transit_routing_preference='less_walking')
            else:
                directions = gmaps.directions(origin=from_string, destination=to_string, mode=method)
            print(directions)
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
        pass

    def _load_youtube_credentials(self):
        client_secret_file = os.getenv('YOUTUBE_CLIENT_SECRET_FILE')
        if not client_secret_file:
            raise Exception(
                "Fichero de Credenciales de Youtube no configuradas.\n"
                "Asegúrate de tener un archivo .env con:\n"
                "YOUTUBE_CLIENT_SECRET_FILE=ruta_del_fichero_json"
            )
        return client_secret_file

    def _load_instagram_credentials(self):
        """Carga las credenciales de Instagram desde el archivo .env"""
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
        return getattr(self, '_instagram_2fa_callback', None)
 
    @instagram_2fa_callback.setter
    def instagram_2fa_callback(self, callback):
        self._instagram_2fa_callback = callback
 
    def _ask_code_2fa_instagram(self):
        """Pide el código 2FA usando el callback registrado, o cae a
        input() por consola si no hay ninguno (uso del modelo sin GUI)."""
        if self.instagram_2fa_callback is not None:
            codigo = self.instagram_2fa_callback()
        else:
            codigo = input(
                "🔐 Instagram pide el código de verificación (2FA). Introdúcelo ahora: "
            )
 
        if not codigo or not codigo.strip():
            raise Exception("No se ha introducido ningún código de verificación de Instagram.")
        return codigo.strip()

    def _get_instagram_client(self):
        """
        Devuelve un cliente de instagrapi ya autenticado, reutilizando
        la sesión guardada si es válida. Si no hay sesión válida, hace
        login completo (pidiendo el código de 2FA vía el callback
        registrado, normalmente una ventana emergente) y guarda la
        sesión para la próxima vez.
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
                print("✅ Instagram: sesión reutilizada (sin pedir 2FA).")
            except Exception as e:
                print(f"⚠️ Instagram: la sesión guardada ya no es válida ({e}). Se requiere login completo.")
                login_via_session = False
        if not login_via_session:
            try:
                client.login(username, password)
            except instagrapi.exceptions.TwoFactorRequired:
                verification_code = self._ask_code_2fa_instagram()
                client.login(username, password, verification_code=verification_code)
            except Exception as e:
                if "two-factor" in str(e).lower() or "2fa" in str(e).lower():
                    verification_code = self._ask_code_2fa_instagram()
                    client.login(username, password, verification_code=verification_code)
                else:
                    raise
            client.dump_settings(INSTAGRAM_SESSION_FILE)
            print("✅ Instagram: login completo y sesión guardada para la próxima vez.")
        return client

    def _upload_to_youtube(self, string_path, string_title, text_description):
        # 1. Autenticación con las librerías modernas
        creds = None
        client_secret_file = self._load_youtube_credentials()
        # Cargar credenciales guardadas
        if os.path.exists(YOUTUBE_SESSION_FLE):
            creds = Credentials.from_authorized_user_file(YOUTUBE_SESSION_FLE)
        # Si no hay credenciales válidas, iniciar flujo OAuth
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secret_file,
                    scopes=['https://www.googleapis.com/auth/youtube.upload']
                )
                creds = flow.run_local_server(port=0)
            # Guardar credenciales para futuras ejecuciones
            with open(YOUTUBE_SESSION_FLE, 'w') as token:
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
        """Método para subir un video a Instagram usando instagrapi."""
        try:
            # Inicializar el cliente de Instagram
            client = self._get_instagram_client()
            # Subir el video
            result = client.clip_upload(string_path,caption=f"{string_title}\n\n{text_description}",)
            print(f"Instagram subido. ID: {result.id}")
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
        # Variable para recoger los datos
        resultados = {'exitosas': [],'fallidas': [],'errores': {}}
        # 0. Verificamos visualmente que todos los datos son correctos
        print('Valor de Path:' + string_path)
        print('Valor de Título:' + string_title)
        print('Valor de GeoLocalización:' + string_location)
        print('Valor de Plataformas:', cb_platforms)
        print('Valor de Descripción:\n' + text_description)

        if "youtube" in cb_platforms:
            try:
                print("\n📤 Subiendo a YOUTUBE...")
                self._upload_to_youtube(string_path, string_title, text_description)
                resultados['exitosas'].append('YouTube')
                print("✅ YouTube: Subida exitosa")
            except Exception as e:
                error_msg = str(e)
                resultados['fallidas'].append('YouTube')
                resultados['errores']['YouTube'] = error_msg
                print(f"❌ YouTube: Error - {error_msg}")
        if "instagram" in cb_platforms:
            try:
                print("\n📤 Subiendo a INSTAGRAM...")
                self._upload_to_instagram(string_path, string_title, text_description)
                resultados['exitosas'].append('Instagram')
                print("✅ Instagram: Subida exitosa")
            except instagrapi.exceptions.LoginRequired:
                error_msg = "La sesión de Instagram ha expirado. Vuelve a iniciar sesión."
                resultados['fallidas'].append('Instagram')
                resultados['errores']['Instagram'] = error_msg
                print(f"❌ Instagram: Error - {error_msg}")
            except instagrapi.exceptions.ClientError as e:
                error_msg = f"Error del cliente de Instagram: {str(e)}"
                resultados['fallidas'].append('Instagram')
                resultados['errores']['Instagram'] = error_msg
                print(f"❌ Instagram: Error - {error_msg}")
            except Exception as e:
                error_msg = f"Error inesperado en Instagram: {str(e)}"
                resultados['fallidas'].append('Instagram')
                resultados['errores']['Instagram'] = error_msg
                print(f"❌ Instagram: Error - {error_msg}")
        return resultados
