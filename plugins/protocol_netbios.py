from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class NetbiosPlugin(BasePlugin):
    name = "NetBIOS"

    def initialize(self, app_context):
        self.app_context = app_context

    def discover(self):
        logger.info("[NetBIOS] Placeholder: descubrimiento de nombres NetBIOS.")
        # Aquí deberías implementar la lógica real usando nmblookup o una librería NetBIOS.
