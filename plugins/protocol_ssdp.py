from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class SsdpPlugin(BasePlugin):
    name = "SSDP"

    def initialize(self, app_context):
        self.app_context = app_context

    def discover(self):
        logger.info("[SSDP] Placeholder: descubrimiento de dispositivos SSDP.")
