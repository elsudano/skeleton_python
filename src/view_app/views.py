#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Vista principal del programa.

Aquí es donde se pondrán los menus de la aplicación junto con los botones,
necesarios para que funcione la primera vista de la aplicación.
"""

import ttkbootstrap as ttk
from src.view_app.view import View

class FirstView(View):
    """Vista Principal del programa."""

    def _init_view(self):
        """Build the home screen's buttons.

        Adds the "Test", "Change Size", "Designer Route" and "Video
        Uploader" buttons on top of the common widgets created by
        `View.__init__`, and binds the shared "Exit" button.
        """
        self._window.set_title("Multiple App Skeleton")
        self.b_test = ttk.Button(self._principal_frame, text="Test", bootstyle='primary')
        self.b_test.grid(column=1, row=1, sticky='NW')
        self.b_test.bind("<Button>", self._controller.test)
        self.b_change_size = ttk.Button(self._principal_frame, text="Change Size", bootstyle='primary')
        self.b_change_size.grid(column=2, row=1, sticky='NW')
        self.b_change_size.bind("<Button>", self._controller.change_size)
        self.b_new_view = ttk.Button(self._principal_frame, text="Designer Route", bootstyle='primary')
        self.b_new_view.grid(column=1, row=2, sticky='NW')
        self.b_new_view.bind("<Button>", self._controller.designer_route)
        self.b_new_view = ttk.Button(self._principal_frame, text="Video Uploader", bootstyle='primary')
        self.b_new_view.grid(column=2, row=2, sticky='NW')
        self.b_new_view.bind("<Button>", self._controller.video_uploader)
        self.b_exit.bind("<Button>", self._controller.exit_application) # este botón es genérico esta en view

class SecondView(View):
    """Vista Principal del programa."""

    def _init_view(self):
        """Build the Tokyo subway route designer screen.

        Adds the title, the "From"/"To"/"Method" fields, and the "Design
        Route" button on top of the common widgets created by
        `View.__init__`.
        """
        self._window.set_size(650,500)
        self._window.set_title("Tokio Subway Designer Route")
        self.b_back = ttk.Button(self._principal_frame, text="Back", bootstyle='warning')
        self.b_back.grid(column=0, row=12, sticky='SW')
        self.b_run = ttk.Button(self._principal_frame, text="Design Route", bootstyle='primary')
        self.b_run.grid(column=11, row=12, sticky='E')
        # Titulo de la ventana
        self.title_label = ttk.Label(self._principal_frame, text="Tokio Subway Designer Route", font=('Arial', 16, 'bold'))
        self.title_label.grid(column=0, row=0, columnspan=12, pady=(0, 20), sticky='W')
        # Titulo del Campo Origen
        self.l_from = ttk.Label(self._principal_frame, text="From:")
        self.l_from.grid(column=1, row=1, columnspan=6, sticky='EW')
        # Campo Origen
        self.e_from = ttk.Entry(self._principal_frame, width=50)
        self.e_from.grid(column=2, row=1, columnspan=12, sticky='EW')
        # Titulo del Campo Destino
        self.l_to = ttk.Label(self._principal_frame, text="To:")
        self.l_to.grid(column=1, row=2, sticky='EW')
        # Campo Destino
        self.e_to = ttk.Entry(self._principal_frame, width=50)
        self.e_to.grid(column=2, row=2, columnspan=12, sticky='EW')
        # Titulo del Campo Método de Transporte
        self.l_method = ttk.Label(self._principal_frame, text="Method:")
        self.l_method.grid(column=1, row=3, sticky='EW')
        # Campo Método de Transporte
        self.cb_method = ttk.Combobox(self._principal_frame, values=['driving','walking','bicycling','transit'])
        self.cb_method.grid(column=2, row=3, columnspan=12, sticky='EW')
        self.b_back.bind("<Button>", self._controller.back)
        self.b_run.bind("<Button>", self._controller.get_directions)
        self.b_exit.bind("<Button>", self._controller.exit_application) # este botón es genérico esta en view

class ThirdView(View):
    """Vista para subir videos a las plataformas de Youtube y Instagram."""

    def _init_view(self):
        """Build the batch video uploader screen.

        Adds the title, the video path/title/geolocation/description
        fields, the YouTube/Instagram checkboxes, and the "Upload Video"
        button on top of the common widgets created by `View.__init__`.
        """
        self._window.set_size(900,700)
        self._window.set_title("Batch Video Uploader")
        self.b_back = ttk.Button(self._principal_frame, text="Back", bootstyle='warning')
        self.b_back.grid(column=0, row=12, sticky='W')
        self.b_run = ttk.Button(self._principal_frame, text="Upload Video", bootstyle='primary')
        self.b_run.grid(column=11, row=12, sticky='E')
        # Titulo de la ventana
        self.title_label = ttk.Label(self._principal_frame, text="Batch Video Uploader", font=('Arial', 16, 'bold'))
        self.title_label.grid(column=0, row=0, columnspan=12, pady=(0, 20), sticky='W')
        # Titulo del Campo Ruta
        self.l_path = ttk.Label(self._principal_frame, text="Video Path:")
        self.l_path.grid(column=1, row=1, sticky='EW')
        # Campo Ruta
        self.e_path = ttk.Entry(self._principal_frame, width=50)
        self.e_path.grid(column=2, row=1, columnspan=10, sticky='EW')
        # Botón para el Path
        self.b_select_file = ttk.Button(self._principal_frame, text="Select File")
        self.b_select_file.grid(column=11, row=1, columnspan=2, sticky='E')
        # Titulo del Campo Título
        self.l_title = ttk.Label(self._principal_frame, text="Title:")
        self.l_title.grid(column=1, row=2, sticky='EW')
        # Campo Título
        self.e_title = ttk.Entry(self._principal_frame, width=50)
        self.e_title.grid(column=2, row=2, columnspan=12, sticky='EW')
        # Título del Campo GeoLocalización
        self.l_geolocation = ttk.Label(self._principal_frame, text="GeoLocation:")
        self.l_geolocation.grid(column=1, row=3, sticky='EW')
        # Campo GeoLocalización
        self.e_geolocation = ttk.Entry(self._principal_frame, width=50)
        self.e_geolocation.grid(column=2, row=3, columnspan=12, sticky='EW')
        # Título del Campo Plataformas
        self.l_platforms = ttk.Label(self._principal_frame,text="Platforms:")
        self.l_platforms.grid(column=1, row=4, sticky='EW')
        # CheckBox de Youtube
        self.cb_youtube = ttk.Checkbutton(self._principal_frame,text="YouTube")
        self.cb_youtube.invoke()
        self.cb_youtube.grid(column=2, row=4, sticky='EW')
        # CheckBox de Instagram
        self.cb_instagram = ttk.Checkbutton(self._principal_frame,text="Instagram")
        self.cb_instagram.invoke()
        self.cb_instagram.grid(column=3, row=4, sticky='EW')
        # Titulo del Campo Descripción
        self.l_description = ttk.Label(self._principal_frame, text="Description:")
        self.l_description.grid(column=1, row=5, sticky='EW')
        # Campo Descripción
        self.tx_description = ttk.ScrolledText(self._principal_frame, width=50, height=5)
        self.tx_description.grid(column=1, row=6, columnspan=13, sticky='EW')
        self.b_back.bind("<Button>", self._controller.back)
        self.b_select_file.bind("<Button>", self._controller._select_file)
        self.b_run.bind("<Button>", self._controller.upload_video)
        self.b_exit.bind("<Button>", self._controller.exit_application) # este botón es genérico esta en view

    def show_instagram_2fa_dialog(self):
        """Show a modal dialog asking for the Instagram 2FA verification code.

        Blocks (via `wait_window()`) until the user confirms or cancels the
        dialog.

        Returns
        -------
        str or None
            The code entered by the user, or None if they cancelled.
        """
        result = {'valor': None}
        modal_view = ttk.Frame(self._window.get())
        modal_view.title("Código de verificación de Instagram")
        modal_view.geometry("340x160")
        modal_view.grab_set()  # modal: bloquea el resto de la app
        modal_view.resizable(False, False)
        ttk.Label(modal_view,text="Instagram requiere el código de verificación (2FA).\nMíralo en tu app de autenticación:",wraplength=300,justify='left',).pack(padx=10, pady=(10, 5), anchor='w')
        modal_input = ttk.Entry(modal_view, width=20)
        modal_input.pack(padx=10, pady=5)
        modal_input.focus_set()
        def confirmar(event=None):
            result['valor'] = modal_input.get().strip()
            modal_view.destroy()
        def cancelar():
            result['valor'] = None
            modal_view.destroy()
        modal_input.bind("<Return>", confirmar)  # Enter también confirma
        modal_bt_frame = ttk.Frame(modal_view)
        modal_bt_frame.pack(pady=10)
        ttk.Button(modal_bt_frame, text="Confirmar", command=confirmar).pack(side='left', padx=5)
        ttk.Button(modal_bt_frame, text="Cancelar", command=cancelar).pack(side='left', padx=5)
        modal_view.wait_window()  # bloquea aquí hasta que se cierre la ventana
        return result['valor']
