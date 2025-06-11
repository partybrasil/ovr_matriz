from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class SoftEtherPlugin(BasePlugin):
    name = "SoftEther"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, config):
        logger.info("[SoftEther] Placeholder: conectar usando configuración SoftEther.")
        # Aquí deberías implementar la lógica real usando la API de SoftEther o comandos de línea.
        self.connected = True

    def disconnect(self):
        self.connected = False
        logger.info("[SoftEther] Disconnected")
