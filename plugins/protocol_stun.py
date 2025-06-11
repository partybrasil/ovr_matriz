from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class StunPlugin(BasePlugin):
    name = "STUN"

    def initialize(self, app_context):
        self.app_context = app_context

    def get_public_ip(self):
        logger.info("[STUN] Placeholder: obtener IP pública y tipo de NAT.")
        return "0.0.0.0", "unknown"
