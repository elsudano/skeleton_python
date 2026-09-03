#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""We have the list of the all controllers that we have in our application.

In this file we will put all the controllers that we need to implement
all the features on our application, that means that we will have
many classes to control all the behavior of our application.
"""

import threading
from src.controller.controller import Controller
from src.model.models import *
from src.view_app.views import *


class FirstController(Controller):

    def back(self, event):
        pass

    def change_size(self, event):
        """Cambiar el tamaño de la Ventana
        Con esto hacemos la prueba de como podemos modificar el padre de la vista.
        """
        if self._window.get_size() != [150,150]:
            self._window.set_size(150, 150)
        else:
            self._window.set_size(600, 350)

    def designer_route(self, event):
        """Cambia la vista de la ventana.
        Con este método pasamos a la aplicación para generar rutas
        en google maps en el metro de Tokio.
        """
        model2 = SecondModel()
        view2 = SecondView(self._window)
        self = SecondController(self._window, view2, model2)

    def video_uploader(self, event):
        """Cambia la vista de la ventana.
        Con este método pasamos a la aplicación de subida de videos
        a las plataformas de forma multiple.
        """
        model3 = ThirdModel()
        view3 = ThirdView(self._window)
        self = ThirdController(self._window, view3, model3)

    def test(self, event):
        """Sirve para realizar test en la parte de la GUI"""
        array_of_events = dir(event)
        for pos in range(len(array_of_events)):
            array_of_events[pos] = 'event.' + array_of_events[pos]
            print('Valor de ' + array_of_events[pos] + ' = ')
            print(array_of_events[pos])


class SecondController(Controller):

    def back(self, event):
        model = FirstModel()
        view = FirstView(self._window)
        self = FirstController(self._window, view, model)

    def get_directions(self, event):
        from_string = self._view.e_from.get()
        to_string = self._view.e_to.get()
        method = self._view.cb_method.get()
        self._model.get_directions(from_string, to_string, method)

class ThirdController(Controller):

    def back(self, event):
        model = FirstModel()
        view = FirstView(self._window)
        self = FirstController(self._window, view, model)

    def _ask_instagram_2fa_code(self):
        """Delega en la Vista la construcción y gestión de la ventana modal."""
        return self._view.show_instagram_2fa_dialog()

    def _select_file(self, event):
        """Abre un diálogo para seleccionar un archivo de video."""
        # Configurar las opciones del diálogo
        file_path = filedialog.askopenfilename(
            title="Select the Video File",
            filetypes=[
                ("Video Files", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv *.webm"),
                ("MP4", "*.mp4"),
                ("AVI", "*.avi"),
                ("MOV", "*.mov"),
                ("MKV", "*.mkv"),
                ("All Files", "*.*")
            ]
        )
        # Si el usuario seleccionó un archivo, actualizar el campo de texto
        if file_path:
            self._view.e_path.delete(0, "")  # Limpiar el campo
            self._view.e_path.insert(0, file_path)  # Insertar la ruta seleccionada

    def upload_video(self, event):
        string_path = self._view.e_path.get()
        string_title = self._view.e_title.get()
        string_location = self._view.e_geolocation.get()
        text_description = self._view.tx_description.get("1.0", tk.END).strip()
        cb_platforms = []
        if self._view.cb_youtube.instate(['selected']):
            cb_platforms.append("youtube")
        if self._view.cb_instagram.instate(['selected']):
            cb_platforms.append("instagram")
        if not cb_platforms:
            self._mostrar_error("Por favor, selecciona al menos una plataforma.")
            return
        if not string_path:
            self._mostrar_error("Por favor, selecciona un archivo de video.")
            return
        self._model.instagram_2fa_callback = self._ask_instagram_2fa_code
        self._view.b_run.state(['disabled'])
        self._view.b_run.config(text="Uploading...")
        def tarea_en_segundo_plano():
            resultados = self._model.upload_video(
                string_path, string_title, string_location, text_description, cb_platforms
            )
            self._window.get().after(0, lambda: self._on_upload_finished(resultados))
        threading.Thread(target=tarea_en_segundo_plano, daemon=True).start()
 
    def _on_upload_finished(self, resultados):
        """Se ejecuta en el hilo principal de Tkinter cuando la subida termina."""
        self._view.b_run.state(['!disabled'])
        self._view.b_run.config(text="Upload Video")
        if resultados['exitosas']:
            print(f"✅ ÉXITO en: {', '.join(resultados['exitosas'])}")
        if resultados['fallidas']:
            print(f"❌ FALLÓ en: {', '.join(resultados['fallidas'])}")
            print("\nDetalles de errores:")
            for plataforma, error in resultados['errores'].items():
                print(f"  • {plataforma}: {error}")
            self._mostrar_error("No se pudo subir en alguna plataforma.")
        else:
            self._clear_fields()

    def _clear_fields(self):
        self._view.e_path.delete(0, "")
        self._view.e_title.delete(0, "")
        self._view.e_geolocation.delete(0, "")
        self._view.tx_description.delete("1.0", tk.END)
        # self._view.cb_youtube.invoke()
        # self._view.cb_instagram.invoke()
        # self._view.cb_tiktok.invoke()
    
    def _mostrar_error(self, mensaje):
        """Muestra un mensaje de error al usuario."""
        from tkinter import messagebox
        messagebox.showerror("Error", mensaje)