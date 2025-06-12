import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QMenuBar, QMenu, QMessageBox
)
from PySide6.QtGui import QAction
from gui.connection_selector import ConnectionSelector
from gui.adapter_verifier import AdapterVerifier
from core.plugin_manager import CorePluginManager
from gui.settings import settings_menu, crear_usuario_interactivo_gui, eliminar_usuario_interactivo_gui
from core.roles import list_users
from core.state_header import StateHeader
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Conexiones")
        self.plugin_manager = CorePluginManager({})
        self.plugin_manager.auto_register_plugins()
        self.app_context = {"current_user": "admin", "plugin_manager": self.plugin_manager}
        self.header_widget = QLabel()
        self.header_widget.setStyleSheet("font-weight: bold; background: #e0e0e0; padding: 6px;")
        self.header_timer = QTimer(self)
        self.header_timer.timeout.connect(self.update_header)
        self.header_timer.start(2000)  # Actualiza cada 2 segundos

        tabs = QTabWidget()
        tabs.addTab(ConnectionSelector(plugin_manager=self.plugin_manager), "Conexión")
        tabs.addTab(AdapterVerifier(), "Adaptadores")

        central = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.header_widget)
        layout.addWidget(tabs)
        central.setLayout(layout)
        self.setCentralWidget(central)
        self.update_header()

    def update_header(self):
        header = StateHeader(self.app_context).get_status()
        text = (
            f"YO: {header['yo']} | RED: {header['red']} | "
            f"PROTOCOLO: {header['protocolo']} | ESTADO: {header['estado']} | "
            f"DESTINO: {header['destino']} | RED DESTINO: {header['red_destino']}"
        )
        self.header_widget.setText(text)

        # Barra de menús
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self._populate_menus()

    def _populate_menus(self):
        # Menú Archivo
        menu_archivo = QMenu("Archivo", self)
        action_salir = QAction("Salir", self)
        action_salir.triggered.connect(self.close)
        menu_archivo.addAction(action_salir)
        self.menu_bar.addMenu(menu_archivo)

        # Menú Usuarios
        menu_usuarios = QMenu("Usuarios", self)
        action_crear_usuario = QAction("Crear usuario", self)
        action_crear_usuario.triggered.connect(lambda: crear_usuario_interactivo_gui(operator=self.app_context["current_user"]))
        action_eliminar_usuario = QAction("Eliminar usuario", self)
        action_eliminar_usuario.triggered.connect(lambda: eliminar_usuario_interactivo_gui(operator=self.app_context["current_user"]))
        action_listar_usuarios = QAction("Listar usuarios", self)
        action_listar_usuarios.triggered.connect(self._mostrar_lista_usuarios)
        menu_usuarios.addAction(action_crear_usuario)
        menu_usuarios.addAction(action_eliminar_usuario)
        menu_usuarios.addAction(action_listar_usuarios)
        self.menu_bar.addMenu(menu_usuarios)

        # Menú Plugins (placeholder*)
        menu_plugins = QMenu("Plugins*", self)
        action_gestor_plugins = QAction("Gestor de plugins*", self)
        action_gestor_plugins.triggered.connect(lambda: settings_menu(self.app_context))
        menu_plugins.addAction(action_gestor_plugins)
        self.menu_bar.addMenu(menu_plugins)

        # Menú Configuración (placeholder*)
        menu_config = QMenu("Configuración*", self)
        action_config = QAction("Abrir configuración*", self)
        action_config.triggered.connect(lambda: settings_menu(self.app_context))
        menu_config.addAction(action_config)
        self.menu_bar.addMenu(menu_config)

        # Menú Ayuda
        menu_ayuda = QMenu("Ayuda", self)
        action_acerca = QAction("Acerca de", self)
        action_acerca.triggered.connect(self._mostrar_acerca)
        menu_ayuda.addAction(action_acerca)
        self.menu_bar.addMenu(menu_ayuda)

    def _mostrar_lista_usuarios(self):
        usuarios = list_users()
        QMessageBox.information(self, "Usuarios registrados", "\n".join(usuarios) if usuarios else "No hay usuarios.")

    def _mostrar_acerca(self):
        QMessageBox.information(self, "Acerca de", "OVR-Matriz\nPlataforma modular de transferencia y control remoto.\nDesarrollado por Insider.")

def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
