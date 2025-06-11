from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class RawSocketPlugin(BasePlugin):
    name = "RawSocket"

    def initialize(self, app_context):
        self.app_context = app_context

    def send_packet(self, interface, packet):
        logger.info(f"[RawSocket] Placeholder: enviar paquete raw en {interface}.")
        # Aquí deberías implementar la lógica real usando sockets raw.
