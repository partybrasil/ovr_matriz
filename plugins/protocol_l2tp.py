from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class L2tpPlugin(BasePlugin):
    name = "L2TP"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, config):
        logger.info("[L2TP] Placeholder: conectar usando configuración L2TP.")
        # Aquí deberías implementar la lógica real para establecer una conexión L2TP.
        # Ejemplo: usar xl2tpd, libreswan, o comandos del sistema.
        self.connected = True

    def disconnect(self):
        self.connected = False
        logger.info("[L2TP] Disconnected")
