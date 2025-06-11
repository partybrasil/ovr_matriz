from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox

class ConnectionSelector(QWidget):
    def __init__(self, parent=None, plugin_manager=None):
        super().__init__(parent)
        self.plugin_manager = plugin_manager
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Selecciona tipo de conexión:"))
        self.combo = QComboBox()
        self.combo.addItems([
            "P2P Directo", "P2P NAT Traversal", "Cliente-Servidor", "Malla (Mesh)",
            "Hub-and-Spoke", "Broadcast/Multicast Virtualizado"
        ])
        layout.addWidget(self.combo)
        self.connect_btn = QPushButton("Conectar")
        layout.addWidget(self.connect_btn)
        self.setLayout(layout)
