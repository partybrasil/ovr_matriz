from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class TurnPlugin(BasePlugin):
    name = "TURN"

    def initialize(self, app_context):
        self.app_context = app_context

    def relay(self, data):
        logger.info("[TURN] Placeholder: retransmitiendo datos a través de TURN.")
        # Aquí deberías implementar la lógica real usando una librería TURN o sockets.
