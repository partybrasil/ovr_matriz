from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class IcePlugin(BasePlugin):
    name = "ICE"

    def initialize(self, app_context):
        self.app_context = app_context

    def negotiate(self):
        logger.info("[ICE] Placeholder: negociación ICE.")
