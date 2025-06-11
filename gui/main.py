import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from gui.connection_selector import ConnectionSelector
from gui.adapter_verifier import AdapterVerifier
from core.plugin_manager import CorePluginManager
from gui.settings import settings_menu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Conexiones")
        self.plugin_manager = CorePluginManager({})
        self.plugin_manager.auto_register_plugins()
        self.app_context = {"current_user": "admin", "plugin_manager": self.plugin_manager}
        tabs = QTabWidget()
        tabs.addTab(ConnectionSelector(plugin_manager=self.plugin_manager), "Conexión")
        tabs.addTab(AdapterVerifier(), "Adaptadores")
        self.setCentralWidget(tabs)
        # Ejemplo: acceso a menú de configuración desde la GUI (en consola)
        # settings_menu(self.app_context)

def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
    main()
