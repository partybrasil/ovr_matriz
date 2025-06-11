from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from gui.connection_selector import ConnectionSelector
from gui.adapter_verifier import AdapterVerifier

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Conexiones")
        tabs = QTabWidget()
        tabs.addTab(ConnectionSelector(), "Conexión")
        tabs.addTab(AdapterVerifier(), "Adaptadores")
        self.setCentralWidget(tabs)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
