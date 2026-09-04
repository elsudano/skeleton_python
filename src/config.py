import os
import sys

if getattr(sys, 'frozen', False):
    # Ejecutando como .exe
    BASE_DIR = os.path.dirname(sys.executable)
    ffmpeg_path = None
    for _filename in os.listdir(sys._MEIPASS):
        if _filename.lower().startswith('ffmpeg'):
            ffmpeg_path = os.path.join(sys._MEIPASS, _filename)
            break
    if ffmpeg_path:
        os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
else:
    # Ejecutando con Python
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_FILE = os.path.join(BASE_DIR, ".env")
CREDENTIALS_DIR = os.path.join(BASE_DIR, ".credentials")
YOUTUBE_CLIENT_SECRET_FILE = os.path.join(CREDENTIALS_DIR, "client_secrets.json")
YOUTUBE_SESSION_FILE = os.path.join(CREDENTIALS_DIR, "youtube_session.json")
INSTAGRAM_SESSION_FILE = os.path.join(CREDENTIALS_DIR, "instagram_session.json")