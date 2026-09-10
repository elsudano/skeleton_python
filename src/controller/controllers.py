#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""We have the list of the all controllers that we have in our application.

In this file we will put all the controllers that we need to implement
all the features on our application, that means that we will have
many classes to control all the behavior of our application.
"""

import threading
from tkinter import filedialog
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import constants
from src.controller.controller import Controller
from src.model.models import (FirstModel, SecondModel, ThirdModel)
from src.view_app.views import (FirstView, SecondView, ThirdView)


class FirstController(Controller):

    def back(self, event):
        """Handle the "Back" action for the main view.

        FirstView is the application's home screen, so there is nowhere to
        go back to; this override intentionally does nothing.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        pass

    def change_size(self, event):
        """Toggle the window size between a small and the default size.

        Demonstrates how the window can be resized programmatically: shrinks
        it to 150x150 if it isn't already that size, otherwise restores it
        to 600x350.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        if self._window.get_size() != [700, 750]:
            self._window.set_size(700, 750)
        else:
            self._window.set_size(600, 350)

    def designer_route(self, event):
        """Switch to the Tokyo subway route designer view.

        Creates a new SecondModel, SecondView and SecondController,
        replacing the current view with the route designer.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        model2 = SecondModel()
        view2 = SecondView(self._window)
        self = SecondController(self._window, view2, model2)

    def video_uploader(self, event):
        """Switch to the batch video uploader view.

        Creates a new ThirdModel, ThirdView and ThirdController, replacing
        the current view with the video uploader.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        model3 = ThirdModel()
        view3 = ThirdView(self._window)
        self = ThirdController(self._window, view3, model3)

    def test(self, event):
        """Dump every attribute of a Tkinter event to the log panel.

        Used to explore what information a given Tkinter event carries,
        useful while developing new bindings.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event to inspect.
        """
        array_of_events = dir(event)
        for pos in range(len(array_of_events)):
            array_of_events[pos] = "event." + array_of_events[pos]
            self.graphical_print("Valor de " + array_of_events[pos] + " = ")
            self.graphical_print(array_of_events[pos])

class SecondController(Controller):

    def back(self, event):
        """Return to the main view from the route designer.

        Rebuilds the main (First) Model, View and Controller and hands
        control back to them, replacing the current Second view.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        model = FirstModel()
        view = FirstView(self._window)
        self = FirstController(self._window, view, model)

    def get_directions(self, event):
        """Compute and log the route between the two entered stations.

        Reads the "From", "To" and "Method" fields from the view and asks
        the Model to fetch the directions from the Google Maps API.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        from_string = self._view.e_from.get()
        to_string = self._view.e_to.get()
        method = self._view.cb_method.get()
        self._model.get_directions(from_string, to_string, method)

class ThirdController(Controller):

    def back(self, event):
        """Return to the main view from the Video Uploader.

        Rebuilds the main (First) Model, View and Controller and hands
        control back to them, replacing the current Second view.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        model = FirstModel()
        view = FirstView(self._window)
        self = FirstController(self._window, view, model)

    def _ask_instagram_2fa_code(self):
        """Ask the user for the Instagram 2FA code from the main thread.

        Registered as `ThirdModel.instagram_2fa_callback`. Since this is
        normally called from the background upload thread, it schedules the
        actual dialog on the main thread via `after()` and blocks (using a
        `threading.Event`) until the user confirms or cancels it.

        Returns
        -------
        str or None
            The code entered by the user, or None if they cancelled.
        """
        resultado = {'valor': None}
        evento = threading.Event()
        def mostrar_dialogo():
            resultado['valor'] = self._view.show_instagram_2fa_dialog()
            evento.set()
        self._window.get().after(0, mostrar_dialogo)
        evento.wait()

        return resultado['valor']

    def _select_file(self, event):
        """Open a file picker and fill in the selected video path.

        Restricts the picker to common video extensions and, if the user
        picks a file, writes its path into the "Video Path" entry field.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
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
        """Validate the upload form and start the video upload in the background.

        Reads all the fields from the view (path, title, location,
        description and selected platforms), validates that at least one
        platform and a video file were chosen, and then launches
        `Model.upload_video` in a background thread so the GUI stays
        responsive while the upload runs.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback.
        """
        string_path = self._view.e_path.get()
        string_title = self._view.e_title.get()
        string_location = self._view.e_geolocation.get()
        text_description = self._view.tx_description.get("1.0", constants.END).strip()
        cb_platforms = []
        if self._view.cb_youtube.instate(['selected']):
            cb_platforms.append("youtube")
        if self._view.cb_instagram.instate(['selected']):
            cb_platforms.append("instagram")
        if not cb_platforms:
            messagebox.showerror("Error", "Por favor, selecciona al menos una plataforma.")
            return
        if not string_path:
            messagebox.showerror("Error", "Por favor, selecciona un archivo de video.")
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
        """Handle the results of a finished video upload.

        Runs on the Tkinter main thread (scheduled via `after()` from the
        background upload thread). Re-enables the "Upload Video" button,
        logs which platforms succeeded or failed, shows an error dialog if
        anything failed, and clears the form on full success.

        Parameters
        ----------
        resultados : dict
            The dict returned by `Model.upload_video`, with 'exitosas',
            'fallidas' and 'errores' keys.
        """
        self._view.b_run.state(['!disabled'])
        self._view.b_run.config(text="Upload Video")
        if resultados['exitosas']:
            self.graphical_print(f"✅ ÉXITO en: {', '.join(resultados['exitosas'])}")
        if resultados['fallidas']:
            self.graphical_print(f"❌ FALLÓ en: {', '.join(resultados['fallidas'])}")
            self.graphical_print("\nDetalles de errores:")
            for plataforma, error in resultados['errores'].items():
                self.graphical_print(f"  • {plataforma}: {error}")
            messagebox.showerror("Error", "No se pudo subir en alguna plataforma.")
        else:
            self._view.e_path.delete(0, constants.END)
            self._view.e_title.delete(0, constants.END)
            self._view.e_geolocation.delete(0, constants.END)
            self._view.tx_description.delete("1.0", constants.END)
            # self._view.cb_youtube.invoke()
            # self._view.cb_instagram.invoke()