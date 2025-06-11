from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class MulticastPlugin(BasePlugin):
    name = "Multicast"

    def initialize(self, app_context):
        self.app_context = app_context

    def send(self, group_ip, data):
        logger.info(f"[Multicast] Placeholder: enviar datos multicast a {group_ip}.")
        # Aquí deberías implementar la lógica real para enviar datos multicast.
