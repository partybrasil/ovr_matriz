from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import sys

class DirectPlayPlugin(BasePlugin):
    name = "DirectPlay"

    def initialize(self, app_context):
        self.app_context = app_context
        self.available = self.is_directplay_available()
        self.connected = False
        if self.available:
            logger.info("[DirectPlay] DirectPlay está disponible.")
        else:
            logger.warning("[DirectPlay] DirectPlay NO está disponible en este sistema.")

    def is_directplay_available(self):
        # Simulación: disponible solo en Windows
        if sys.platform.startswith("win"):
            return True
        return False

    def connect(self, host, port):
        if not self.available:
            logger.warning("[DirectPlay] No disponible, no se puede conectar.")
            return False
        if not has_permission(self.app_context.get("role", "user"), "connect_directplay"):
            logger.warning("[DirectPlay] No permission to use DirectPlay.")
            return False
        # Lógica real de conexión DirectPlay (placeholder)
        self.connected = True
        logger.info(f"[DirectPlay] Conectado a {host}:{port} (simulado)")
        return True

    def disconnect(self):
        self.connected = False
        logger.info("[DirectPlay] Desconectado (simulado)")
