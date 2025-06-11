from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class NatAdapterPlugin(BasePlugin):
    name = "NATAdapter"

    def initialize(self, app_context):
        self.app_context = app_context

    def check_adapters(self):
        logger.info("[NATAdapter] Placeholder: verificar adaptadores de red y reglas NAT.")
