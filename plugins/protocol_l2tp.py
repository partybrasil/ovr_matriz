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
        self.connected = True

    def disconnect(self):
        self.connected = False
        logger.info("[L2TP] Disconnected")
