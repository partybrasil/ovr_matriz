from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class IpSecPlugin(BasePlugin):
    name = "IPSec"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, config):
        logger.info("[IPSec] Placeholder: conectar usando configuración IPSec.")
        self.connected = True

    def disconnect(self):
        self.connected = False
        logger.info("[IPSec] Disconnected")
