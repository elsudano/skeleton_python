# Python Gui Skeleton

> ⚠️ **Proyecto en desarrollo.** Este repositorio es una *plantilla base* (skeleton) para arrancar rápidamente aplicaciones de escritorio en Python con interfaz gráfica, siguiendo un patrón **MVC** (Modelo-Vista-Controlador). Actualmente incluye, a modo de ejemplo funcional, un módulo de subida de vídeos a YouTube e Instagram, pero el objetivo del repositorio es servir de esqueleto reutilizable sobre el que añadir nuevas funcionalidades.

## Índice

- [Objetivo del proyecto](#objetivo-del-proyecto)
- [Arquitectura](#arquitectura)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Módulos incluidos actualmente](#módulos-incluidos-actualmente)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Generar el binario (PyInstaller)](#generar-el-binario-pyinstaller)
- [Cómo añadir una nueva funcionalidad](#cómo-añadir-una-nueva-funcionalidad)
- [Estado del proyecto / roadmap](#estado-del-proyecto--roadmap)
- [Licencia](LICENSE)

## Objetivo del proyecto

`skeleton_python` nace como una base reutilizable para crear aplicaciones de escritorio multiplataforma (Windows y Linux) con Python. Su propósito **no** es resolver un único caso de uso, sino ofrecer:

- Una arquitectura MVC ya montada y desacoplada (Modelo / Vista / Controlador).
- Una ventana principal con menú (`File`, `Edit`, `Show`, `Tools`) lista para extender.
- Un mecanismo sencillo para añadir nuevas "pantallas" (cada una con su propio Modelo, Vista y Controlador) sin tocar el resto de la aplicación.
- Un sistema de configuración centralizado (rutas, credenciales) que funciona igual en modo desarrollo (`python main.py`) y en modo binario empaquetado (PyInstaller).

Sobre esta base se han ido añadiendo módulos de ejemplo para validar el patrón (ver [Módulos incluidos actualmente](#módulos-incluidos-actualmente)).

## Arquitectura

El proyecto sigue el patrón **MVC**, con una capa adicional de abstracción de la "ventana":

```
Window  ──▶  View  ◀──▶  Controller  ◀──▶  Model
```

- **`Window`** (`src/view_app/window.py`): envoltorio sobre la ventana raíz de `ttkbootstrap`/`tkinter`. Gestiona tamaño, posición, título y ciclo de vida (`start`/`stop`).
- **`View`** (`src/view_app/view.py`): clase base abstracta de la que heredan todas las vistas. Se encarga de la barra de menús y de delegar la construcción de cada pantalla concreta en `_init_view()`.
- **`Controller`** (`src/controller/controller.py`): clase base abstracta que conecta una `View` con su `Model`, registra las acciones del menú y expone los métodos comunes (nuevo, abrir, guardar, salir...).
- **`Model`** (`src/model/model.py`): clase base abstracta responsable de la lógica de negocio y del acceso a datos/credenciales (carga variables desde `.env`).

Cada "pantalla" de la aplicación (por ejemplo, el subidor de vídeos) se implementa como una tríada `XxxModel` / `XxxView` / `XxxController` que hereda de estas clases base, y que se puede sustituir en caliente dentro de la misma ventana.

## Estructura del repositorio

```
.
├── main.py                # Punto de entrada de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── skeleton_python.spec   # Configuración de empaquetado con PyInstaller
├── src/
│   ├── config.py          # Rutas y configuración centralizada (dev vs. binario)
│   ├── model/
│   │   ├── model.py       # Clase base Model (ABC)
│   │   └── models.py      # Modelos concretos (First/Second/Third)
│   ├── controller/
│   │   ├── controller.py  # Clase base Controller (ABC)
│   │   └── controllers.py # Controladores concretos (First/Second/Third)
│   └── view_app/
│       ├── view.py        # Clase base View (ABC)
│       ├── views.py       # Vistas concretas (First/Second/Third)
│       ├── widgets.py     # Widgets auxiliares reutilizables
│       └── window.py      # Envoltorio de la ventana principal
└── assets/
    ├── thumbnail.jpg       # Recurso usado por el módulo de Instagram
    ├── icon.png            # Recurso usado por Pyinstaller
    └── icon.ico            # Recurso usado por Pyinstaller
```

> El proyecto está preparado para admitir en el futuro otro tipo de interfaces (por ejemplo, una vista web en un directorio `view_web`) sin cambiar la lógica de modelo/controlador.

## Módulos incluidos actualmente

| Pantalla | Model / View / Controller | Descripción |
|---|---|---|
| Menú principal | `FirstModel` / `FirstView` / `FirstController` | Ventana inicial con accesos a los distintos módulos de ejemplo. |
| Generador de rutas | `SecondModel` / `SecondView` / `SecondController` | Prueba de concepto para calcular rutas con la API de Google Maps y exportarlas a KML (`simplekml`). Módulo experimental, pendiente de terminar. |
| Subida de vídeos | `ThirdModel` / `ThirdView` / `ThirdController` | Sube un mismo vídeo a **YouTube** (API oficial vía OAuth) e **Instagram** (vía `instagrapi`, con soporte de doble factor de autenticación) desde un único formulario. La subida se ejecuta en un hilo aparte para no bloquear la interfaz. |

Estos módulos sirven como referencia de cómo montar una nueva funcionalidad completa sobre el esqueleto; no forman parte del "núcleo" reutilizable del proyecto.

## Requisitos

- Python 3.10+ (recomendado)
- pip
- Cuenta de Google Cloud con la API de YouTube Data v3 habilitada (solo si se usa el módulo de subida a YouTube)
- Cuenta de Instagram (solo si se usa el módulo de subida a Instagram)
- Clave de API de Google Maps (solo si se usa el módulo de rutas)

## Instalación

```bash
git clone https://github.com/elsudano/skeleton_python.git
cd skeleton_python
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuración

La aplicación busca un fichero `.env` en la raíz del proyecto (o junto al ejecutable, si se ha empaquetado con PyInstaller). Crea uno a partir de este ejemplo:

```dotenv
# YouTube
YOUTUBE_CLIENT_SECRET_FILE=.credentials/client_secrets.json

# Instagram
INSTAGRAM_USERNAME=tu_usuario
INSTAGRAM_PASSWORD=tu_contraseña

# Google Maps (módulo de rutas)
GMAPS_API_KEY=tu_api_key
```

Las credenciales de YouTube (`client_secrets.json`) y las sesiones generadas (tokens/cookies) se guardan en el directorio `.credentials/`, que está excluido del control de versiones (`.gitignore`).

Todas las rutas se resuelven de forma centralizada en `src/config.py`, que detecta automáticamente si la aplicación se ejecuta desde código fuente o desde un binario generado con PyInstaller.

## Uso

```bash
python main.py
```

Se abrirá la ventana principal, desde la que se puede navegar a los distintos módulos de ejemplo mediante los botones disponibles.

## Generar el binario (PyInstaller)

El proyecto incluye un fichero `skeleton_python.spec` ya configurado (incluye recursos como `thumbnail.jpg` y las dependencias necesarias de `google-api` e `instagrapi`).

```bash
pip install pyinstaller
pyinstaller --clean --noconfirm skeleton_python.spec
```

El binario resultante se genera en `dist/`. Recuerda copiar junto al ejecutable el fichero `.env` (y, si aplica, el directorio `.credentials/`) para que la configuración se cargue correctamente.

## Cómo añadir una nueva funcionalidad

Gracias al patrón MVC, añadir una nueva pantalla no requiere tocar el resto de la aplicación:

1. **Modelo**: crea una nueva clase en `src/model/models.py` que herede de `Model` e implemente `hacer_algo()` junto con la lógica que necesites.
2. **Vista**: crea una nueva clase en `src/view_app/views.py` que herede de `View` e implemente `_init_view()` con los widgets de tu pantalla.
3. **Controlador**: crea una nueva clase en `src/controller/controllers.py` que herede de `Controller` e implemente `back()` (para volver a la pantalla anterior) y los métodos que conecten los widgets de tu vista con tu modelo.
4. **Navegación**: añade un botón o entrada de menú en la vista desde la que se debe acceder a tu nueva pantalla, siguiendo el mismo patrón que `video_uploader()` o `designer_route()` en `FirstController`.

## Estado del proyecto / roadmap

Este repositorio está en desarrollo activo. Algunos puntos conocidos pendientes:

- Terminar el módulo de generación de rutas (`SecondModel`/`SecondView`).
- Completar las acciones del menú principal (`New`, `Open`, `Save`, `Cut`, `Copy`, `Paste`, marcadas como `FIXME` en el código).
- Añadir tests automatizados.

Las contribuciones y sugerencias son bienvenidas mientras el esqueleto va tomando forma.
