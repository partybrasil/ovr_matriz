import sys
from core.plugin_manager import CorePluginManager
from core.logger import logger
from core.roles import has_permission
from config.settings import settings

# Importa los módulos CLI y GUI
from cli.main import main as cli_main
from gui.main import main as gui_main

def run_gui():
    gui_main()

def run_cli():
    cli_main()

def ask_mode():
    from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
    import sys

    class ModeDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Seleccionar versión")
            self.selected = None
            layout = QVBoxLayout()
            label = QLabel("¿Qué versión deseas iniciar?")
            layout.addWidget(label)
            btn_gui = QPushButton("GUI")
            btn_cli = QPushButton("CLI")
            btn_gui.clicked.connect(self.select_gui)
            btn_cli.clicked.connect(self.select_cli)
            layout.addWidget(btn_gui)
            layout.addWidget(btn_cli)
            self.setLayout(layout)

        def select_gui(self):
            self.selected = "gui"
            self.accept()

        def select_cli(self):
            self.selected = "cli"
            self.accept()

    app = QApplication(sys.argv)
    dialog = ModeDialog()
    if dialog.exec() == QDialog.Accepted:
        mode = dialog.selected
    else:
        return  # Si se cancela el diálogo, salir de la función

    return mode

def main():
    # Contexto global de la app
    app_context = {
        "role": "admin",
        "protocol": "none",
        "settings": settings
    }

    # Inicializa el gestor de plugins del core (auto-descubrimiento)
    plugin_manager = CorePluginManager(app_context)
    plugin_manager.auto_register_plugins()
    app_context["plugin_manager"] = plugin_manager

    # Selección de modo de inicio
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
    else:
        mode = ask_mode()
        if mode is not None:
            mode = mode.lower()
    if mode == "gui":
        run_gui()
    elif mode == "cli":
        run_cli()
    else:
        print("Por favor, elige 'gui' o 'cli'.")

if __name__ == "__main__":
    main()
