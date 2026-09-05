import os
import sys

if getattr(sys, 'frozen', False):
    # Ejecutando como .exe
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # Ejecutando con Python
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_FILE = os.path.join(BASE_DIR, ".env")
CREDENTIALS_DIR = os.path.join(BASE_DIR, ".credentials")
YOUTUBE_CLIENT_SECRET_FILE = os.path.join(CREDENTIALS_DIR, "client_secrets.json")
YOUTUBE_SESSION_FILE = os.path.join(CREDENTIALS_DIR, "youtube_session.json")
INSTAGRAM_SESSION_FILE = os.path.join(CREDENTIALS_DIR, "instagram_session.json")