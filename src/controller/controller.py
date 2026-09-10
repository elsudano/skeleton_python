#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Controlador principal del programa.

Con esto se pretende abstraer la parte de la vista del programa así pues,
se genera un controlador que se encarga de todas las vistas del programa.
"""

from abc import ABC, abstractmethod


class Controller(ABC):
    """Clase controlador."""

    _window = None  # Tipo ventana y se crea vacío.
    _model = None  # This save the model of the application
    _view = None  # This save the view of the current application status

    def __init__(self, window, view, model):
        """Wire up the Window, View and Model for this controller.

        This is the base constructor shared by every concrete Controller. It
        stores the references to the Window, View and Model, connects the
        Model's `log_callback` to this controller's `graphical_print` (see
        model.py for why this indirection is needed to respect MVC), builds
        the whole menu bar by delegating each menu item to the corresponding
        `menu_item_*` method, and finally calls `View._init_view()` to let
        the concrete View create its own widgets.

        Parameters
        ----------
        window : Window
            The main application Window shared across all views.
        view : View
            The concrete View this controller will manage.
        model : Model
            The concrete Model this controller will manage.
        """
        self._window = window
        self._view = view
        self._model = model
        self._view._set_controller(self)
        # con lo siguiente generamos toda la barra de menus que se ha creado para la vista
        self._view._add_item_menu("File", "New", self.menu_item_new)
        self._view._add_item_menu("File", "Open", self.menu_item_open)
        self._view._add_item_menu("File", "Save", self.menu_item_save)
        self._view._add_item_menu("File", "Exit", self.menu_item_exit)
        self._view._add_item_menu("Edit", "Cut", self.menu_item_cut)
        self._view._add_item_menu("Edit", "Copy", self.menu_item_copy)
        self._view._add_item_menu("Edit", "Paste", self.menu_item_paste)
        self._view._add_item_menu("Show", "Tool Bar", self.menu_item_show_tools_bar)
        self._view._add_item_menu("Show", "Status Bar", self.menu_item_show_status_bar)
        self._view._add_item_menu("Tools", "Change Theme", self.menu_item_change_theme)
        self._view._add_item_menu("Tools", "Utilities", self.menu_item_other)
        self._view._init_view()
        self._model.log_callback = self.graphical_print
        for menu in self._view._menus:
            self._view._menu_bar.add_cascade(label=menu.cget('title'), menu=menu)

    @abstractmethod
    def back(self, event):
        """Handle the "Back" action for this controller's view.

        Abstract method that every concrete Controller must implement to
        define what happens when the user navigates back to the previous
        view. Called from the "Back" button bound in the corresponding View.

        Parameters
        ----------
        event : tkinter.Event
            The Tkinter event that triggered this callback (e.g. a button click).
        """
        pass

    def graphical_print(self, message):
        """Send a message to the View's log panel.

        This is the single entry point through which any message reaches the
        GUI log panel - both the ones this Controller generates directly and
        the ones that arrive from the Model through `log_callback` (see
        Model.log_callback in model.py).

        It can be called both from the main thread (e.g. a button click, or
        SecondModel.get_directions) and from a background thread (e.g.
        ThirdModel.upload_video, which runs inside a threading.Thread).
        Since Tkinter is not thread-safe, this always dispatches the update
        through `after()`, so the widget is only ever touched from the main
        thread, no matter which thread called this method.

        Parameters
        ----------
        message : str
            The message that will be shown in the logs console.
        """
        self._window.get().after(0, self._view._append_log, message)

    def menu_item_new(self):
        """Handle the "File > New" menu action.

        Placeholder for the logic that should run when the user selects
        File > New. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Nuevo
        pass

    def menu_item_open(self):
        """Handle the "File > Open" menu action.

        Placeholder for the logic that should run when the user selects
        File > Open. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Abrir
        pass

    def menu_item_save(self):
        """Handle the "File > Save" menu action.

        Placeholder for the logic that should run when the user selects
        File > Save. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Guardar
        pass

    def menu_item_cut(self):
        """Handle the "Edit > Cut" menu action.

        Placeholder for the logic that should run when the user selects
        Edit > Cut. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Cortar
        pass

    def menu_item_copy(self):
        """Handle the "Edit > Copy" menu action.

        Placeholder for the logic that should run when the user selects
        Edit > Copy. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Copiar
        pass

    def menu_item_paste(self):
        """Handle the "Edit > Paste" menu action.

        Placeholder for the logic that should run when the user selects
        Edit > Paste. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Pegar
        pass

    def menu_item_show_tools_bar(self):
        """Handle the "Show > Tool Bar" menu action.

        Placeholder for the logic that should run when the user selects
        Show > Tool Bar. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Ver/Mostrar barra de herramientas
        pass

    def menu_item_show_status_bar(self):
        """Handle the "Show > Status Bar" menu action.

        Placeholder for the logic that should run when the user selects
        Show > Status Bar. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Ver/Mostrar barra de estado
        pass

    def menu_item_change_theme(self):
        """Handle the "Tools > Change Theme" menu action, toggle between the light and dark theme.

        Switches the whole application between the "superhero" (light-ish)
        and "darkly" (dark) ttkbootstrap themes every time it is called.
        """
        if self._window.get_theme() == "superhero":
            self._window.set_theme("darkly")
        else:
            self._window.set_theme("superhero")

    def menu_item_other(self):
        """Handle the "Tools > Utilities" menu action.

        Placeholder for the logic that should run when the user selects
        Tools > Utilities. Not implemented yet.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Herramientas/Útiles
        pass

    def menu_item_exit(self):
        """Handle the "File > Exit" menu action.

        Delegates to `exit_application` to close the app, the same as
        pressing the window's Exit button.
        """
        self.exit_application(None)

    def exit_application(self, event):
        """Stop the application.

        Stops the Tkinter main loop via `Window.stop()`, effectively closing
        the application window.

        Parameters
        ----------
        event : tkinter.Event or None
            The Tkinter event that triggered this callback (e.g. a button
            click), or None when called directly (e.g. from a menu item).
        """
        self._window.stop()