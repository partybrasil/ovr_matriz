from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class MulticastPlugin(BasePlugin):
    name = "Multicast Virtual"

    def initialize(self, app_context):
        self.app_context = app_context

    def send(self, data):
        logger.info("[Multicast] Placeholder: enviar datos multicast virtual.")
