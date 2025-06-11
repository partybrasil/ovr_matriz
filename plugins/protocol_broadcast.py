from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class BroadcastPlugin(BasePlugin):
    name = "Broadcast Virtual"

    def initialize(self, app_context):
        self.app_context = app_context

    def send(self, data):
        logger.info("[Broadcast] Placeholder: enviar datos broadcast virtual.")
