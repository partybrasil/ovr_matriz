import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QMenuBar, QMenu, QMessageBox,
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QGridLayout, QSizePolicy, QScrollArea
)
from PySide6.QtGui import QAction, QPixmap, QIcon, QColor
from PySide6.QtCore import QTimer, Qt

from gui.connection_selector import ConnectionSelector
from gui.adapter_verifier import AdapterVerifier
from core.plugin_manager import CorePluginManager
from gui.settings import settings_menu, crear_usuario_interactivo_gui, eliminar_usuario_interactivo_gui
from core.roles import list_users
from core.state_header import StateHeader

class PluginManagerWindow(QDialog):
    def __init__(self, plugin_manager, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gestor de Plugins")
        self.plugin_manager = plugin_manager
        self.setMinimumWidth(700)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        grid = QGridLayout()
        plugins = sorted(self.plugin_manager.get_all_plugin_info(), key=lambda x: x["name"].lower())
        icons = {
            "ok": QIcon(self._make_pixmap(Qt.green, "✔")),
            "inactive": QIcon(self._make_pixmap(Qt.red, "✖")),
            "warning": QIcon(self._make_pixmap(Qt.yellow, "!")),
        }
        # 3 columnas
        col_count = 3
        for idx, info in enumerate(plugins):
            row, col = divmod(idx, col_count)
            # Estado
            if info["active"]:
                icon = icons["ok"]
                state_text = "Conectado"
                color = "#4caf50"
            else:
                icon = icons["inactive"]
                state_text = "Inactivo"
                color = "#f44336"
            # Si el plugin tiene un atributo 'status' y es 'warning', mostrar advertencia
            plugin_obj = self.plugin_manager.get_plugin(info["name"])
            if hasattr(plugin_obj, "status") and getattr(plugin_obj, "status", "") == "warning":
                icon = icons["warning"]
                state_text = "Problema"
                color = "#ffeb3b"
            # Widget de plugin
            plugin_widget = QWidget()
            plugin_layout = QVBoxLayout()
            plugin_layout.setAlignment(Qt.AlignTop)
            # Icono y nombre
            icon_label = QLabel()
            icon_label.setPixmap(icon.pixmap(32, 32))
            icon_label.setAlignment(Qt.AlignCenter)
            name_label = QLabel(f"<b>{info['name']}</b>")
            name_label.setAlignment(Qt.AlignCenter)
            # Estado
            state_label = QLabel(state_text)
            state_label.setAlignment(Qt.AlignCenter)
            state_label.setStyleSheet(f"background: {color}; color: black; border-radius: 6px; padding: 2px 8px;")
            # Botón inicializar
            btn = QPushButton("Inicializar")
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, n=info["name"]: self._inicializar_plugin(n))
            # Añadir al layout
            plugin_layout.addWidget(icon_label)
            plugin_layout.addWidget(name_label)
            plugin_layout.addWidget(state_label)
            plugin_layout.addWidget(btn)
            plugin_widget.setLayout(plugin_layout)
            grid.addWidget(plugin_widget, row, col)
        content.setLayout(grid)
        scroll.setWidget(content)
        layout.addWidget(scroll)
        self.setLayout(layout)

    def _make_pixmap(self, color, text):
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.transparent)
        from PySide6.QtGui import QPainter, QFont
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(color))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, 32, 32)
        painter.setPen(Qt.black)
        font = QFont()
        font.setBold(True)
        font.setPointSize(18)
        painter.setFont(font)
        painter.drawText(pixmap.rect(), Qt.AlignCenter, text)
        painter.end()
        return pixmap

    def _inicializar_plugin(self, name):
        plugin = self.plugin_manager.get_plugin(name)
        if plugin:
            plugin.activate()
            QMessageBox.information(self, "Plugin", f"Plugin '{name}' inicializado/activado.")
            self.close()
            # Reabrir para refrescar estados
            dlg = PluginManagerWindow(self.plugin_manager, self.parent())
            dlg.exec()

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
        self._create_menus()

    def update_header(self):
        header = StateHeader(self.app_context).get_status()
        text = (
            f"YO: {header['yo']} | RED: {header['red']} | "
            f"PROTOCOLO: {header['protocolo']} | ESTADO: {header['estado']} | "
            f"DESTINO: {header['destino']} | RED DESTINO: {header['red_destino']}"
        )
        self.header_widget.setText(text)

    def _create_menus(self):
        menubar = QMenuBar(self)
        # Menú Archivo
        menu_archivo = QMenu("Archivo", self)
        action_salir = QAction("Salir", self)
        action_salir.triggered.connect(self.close)
        menu_archivo.addAction(action_salir)
        menubar.addMenu(menu_archivo)

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
        menubar.addMenu(menu_usuarios)

        # Menú Plugins (solo abre la ventana)
        menu_plugins = QMenu("Plugins", self)
        action_gestor_plugins = QAction("Gestor de plugins...", self)
        action_gestor_plugins.triggered.connect(self._abrir_gestor_plugins)
        menu_plugins.addAction(action_gestor_plugins)
        menubar.addMenu(menu_plugins)

        # Menú Configuración
        menu_config = QMenu("Configuración", self)
        menu_config.addAction(QAction("General", self, triggered=self._show_config_placeholder))
        menu_config.addAction(QAction("Avanzado", self, triggered=self._show_config_placeholder))
        menu_config.addAction(QAction("Preferencias de usuario", self, triggered=self._show_config_placeholder))
        menu_config.addAction(QAction("Idioma", self, triggered=self._show_config_placeholder))
        menu_config.addAction(QAction("Seguridad", self, triggered=self._show_config_placeholder))
        menubar.addMenu(menu_config)

        # Menú Ayuda
        menu_ayuda = QMenu("Ayuda", self)
        action_acerca = QAction("Acerca de", self)
        action_acerca.triggered.connect(self._mostrar_acerca)
        menu_ayuda.addAction(action_acerca)
        menubar.addMenu(menu_ayuda)

        self.setMenuBar(menubar)

    def _abrir_gestor_plugins(self):
        dlg = PluginManagerWindow(self.plugin_manager, self)
        dlg.exec()

    def _mostrar_lista_usuarios(self):
        usuarios = list_users()
        QMessageBox.information(self, "Usuarios registrados", "\n".join(usuarios) if usuarios else "No hay usuarios.")

    def _mostrar_acerca(self):
        QMessageBox.information(self, "Acerca de", "OVR-Matriz\nPlataforma modular de transferencia y control remoto.\nDesarrollado por Insider.")

    def _show_config_placeholder(self):
        QMessageBox.information(self, "Configuración", "Funcionalidad de configuración aún no implementada (placeholder).")

def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
