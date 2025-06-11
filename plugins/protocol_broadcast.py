from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class BroadcastPlugin(BasePlugin):
    name = "Broadcast"

    def initialize(self, app_context):
        self.app_context = app_context

    def send(self, data):
        logger.info("[Broadcast] Placeholder: enviar datos broadcast virtualmente.")
        # Aquí deberías implementar la lógica real para enviar datos broadcast.
