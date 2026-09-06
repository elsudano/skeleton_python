# Python GUI skeleton

[Spanish Version of README](README_es.md)

> ⚠️ **Work in progress.** This repository is a base *skeleton* for quickly bootstrapping desktop applications in Python with a graphical interface, following an **MVC** (Model-View-Controller) pattern. It currently includes, as a working example, a module for uploading videos to YouTube and Instagram, but the goal of the repository is to serve as a reusable skeleton on top of which new features can be added.

## Table of contents

- [Project goal](#project-goal)
- [Architecture](#architecture)
- [Repository structure](#repository-structure)
- [Modules currently included](#modules-currently-included)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Building the binary (PyInstaller)](#building-the-binary-pyinstaller)
- [How to add a new feature](#how-to-add-a-new-feature)
- [Project status / roadmap](#project-status--roadmap)
- [License](LICENSE)

## Project goal

`skeleton_python` was created as a reusable base for building cross-platform (Windows and Linux) desktop applications with Python. Its purpose is **not** to solve a single use case, but to provide:

- An already-wired, decoupled MVC architecture (Model / View / Controller).
- A main window with a menu (`File`, `Edit`, `Show`, `Tools`) ready to be extended.
- A simple mechanism to add new "screens" (each with its own Model, View and Controller) without touching the rest of the application.
- A centralized configuration system (paths, credentials) that works the same way in development mode (`python main.py`) and in a packaged binary (PyInstaller).

On top of this base, a few example modules have been added to validate the pattern (see [Modules currently included](#modules-currently-included)).

## Architecture

The project follows the **MVC** pattern, with an additional abstraction layer for the "window":

```
Window  ──▶  View  ◀──▶  Controller  ◀──▶  Model
```

- **`Window`** (`src/view_app/window.py`): wrapper around the root window of `ttkbootstrap`/`tkinter`. Handles size, position, title and lifecycle (`start`/`stop`).
- **`View`** (`src/view_app/view.py`): abstract base class inherited by every view. Handles the menu bar and delegates the construction of each concrete screen to `_init_view()`.
- **`Controller`** (`src/controller/controller.py`): abstract base class that connects a `View` with its `Model`, registers menu actions and exposes common methods (new, open, save, exit...).
- **`Model`** (`src/model/model.py`): abstract base class responsible for business logic and data/credentials access (loads environment variables from `.env`).

Each "screen" of the application (for example, the video uploader) is implemented as an `XxxModel` / `XxxView` / `XxxController` triad that inherits from these base classes, and can be swapped in and out of the same window at runtime.

## Repository structure

```
.
├── main.py                        # Application entry point
├── requirements.txt                # Project dependencies
├── skeleton_python.spec            # PyInstaller packaging configuration
├── thumbnail.jpg                   # Resource used by the Instagram module
└── src/
    ├── config.py                   # Centralized paths and configuration (dev vs. binary)
    ├── model/
    │   ├── model.py                 # Base Model class (ABC)
    │   └── models.py                # Concrete models (First/Second/Third)
    ├── controller/
    │   ├── controller.py            # Base Controller class (ABC)
    │   └── controllers.py           # Concrete controllers (First/Second/Third)
    └── view_app/
        ├── view.py                  # Base View class (ABC)
        ├── views.py                  # Concrete views (First/Second/Third)
        ├── widgets.py                 # Reusable auxiliary widgets
        └── window.py                  # Main window wrapper
```

> The project is designed to support other types of interfaces in the future (for example, a web view under a `view_web` directory) without changing the model/controller logic.

## Modules currently included

| Screen | Model / View / Controller | Description |
|---|---|---|
| Main menu | `FirstModel` / `FirstView` / `FirstController` | Initial window with access to the different example modules. |
| Route generator | `SecondModel` / `SecondView` / `SecondController` | Proof of concept to calculate routes with the Google Maps API and export them to KML (`simplekml`). Experimental module, still unfinished. |
| Video uploader | `ThirdModel` / `ThirdView` / `ThirdController` | Uploads the same video to **YouTube** (official API via OAuth) and **Instagram** (via `instagrapi`, with two-factor authentication support) from a single form. The upload runs on a separate thread so it doesn't block the UI. |

These modules act as a reference for how to build a complete new feature on top of the skeleton; they are not part of the reusable "core" of the project.

## Requirements

- Python 3.10+ (recommended)
- pip
- A Google Cloud account with the YouTube Data API v3 enabled (only if using the YouTube upload module)
- An Instagram account (only if using the Instagram upload module)
- A Google Maps API key (only if using the routes module)

## Installation

```bash
git clone https://github.com/elsudano/skeleton_python.git
cd skeleton_python
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

The application looks for a `.env` file in the project root (or next to the executable, when packaged with PyInstaller). Create one based on this example:

```dotenv
# YouTube
YOUTUBE_CLIENT_SECRET_FILE=.credentials/client_secrets.json

# Instagram
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password

# Google Maps (routes module)
GMAPS_API_KEY=your_api_key
```

YouTube credentials (`client_secrets.json`) and generated sessions (tokens/cookies) are stored in the `.credentials/` directory, which is excluded from version control (`.gitignore`).

All paths are resolved centrally in `src/config.py`, which automatically detects whether the application is running from source or from a binary built with PyInstaller.

## Usage

```bash
python main.py
```

This opens the main window, from which you can navigate to the different example modules using the available buttons.

## Building the binary (PyInstaller)

The project includes an already configured `skeleton_python.spec` file (it includes resources such as `thumbnail.jpg` and the required `google-api` and `instagrapi` dependencies).

```bash
pip install pyinstaller
pyinstaller --clean --noconfirm skeleton_python.spec
```

The resulting binary is generated in `dist/`. Remember to copy the `.env` file (and the `.credentials/` directory, if applicable) next to the executable so the configuration loads correctly.

## How to add a new feature

Thanks to the MVC pattern, adding a new screen doesn't require touching the rest of the application:

1. **Model**: create a new class in `src/model/models.py` that inherits from `Model` and implements `hacer_algo()` along with the logic you need.
2. **View**: create a new class in `src/view_app/views.py` that inherits from `View` and implements `_init_view()` with your screen's widgets.
3. **Controller**: create a new class in `src/controller/controllers.py` that inherits from `Controller` and implements `back()` (to return to the previous screen) and the methods that connect your view's widgets to your model.
4. **Navigation**: add a button or menu entry in the view from which your new screen should be reachable, following the same pattern as `video_uploader()` or `designer_route()` in `FirstController`.

## Project status / roadmap

This repository is under active development. Some known pending items:

- Finish the route generation module (`SecondModel`/`SecondView`).
- Complete the main menu actions (`New`, `Open`, `Save`, `Cut`, `Copy`, `Paste`, marked as `FIXME` in the code).
- Add automated tests.

Contributions and suggestions are welcome while the skeleton takes shape.