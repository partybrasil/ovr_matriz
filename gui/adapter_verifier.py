from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class AdapterVerifier(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Verificar adaptadores de red y reglas NAT"))
        self.verify_btn = QPushButton("Verificar")
        layout.addWidget(self.verify_btn)
        self.setLayout(layout)
