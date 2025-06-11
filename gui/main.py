from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from gui.connection_selector import ConnectionSelector
from gui.adapter_verifier import AdapterVerifier
from plugins.plugin_manager import PluginManager
from plugins.protocol_vxlan import VxlanPlugin

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Conexiones")
        self.plugin_manager = PluginManager({})
        self.plugin_manager.register(VxlanPlugin())
        tabs = QTabWidget()
        tabs.addTab(ConnectionSelector(self.plugin_manager), "Conexión")
        tabs.addTab(AdapterVerifier(), "Adaptadores")
        self.setCentralWidget(tabs)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
