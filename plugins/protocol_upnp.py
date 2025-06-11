from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class UpnpPlugin(BasePlugin):
    name = "UPnP"

    def initialize(self, app_context):
        self.app_context = app_context

    def open_port(self, port, protocol="TCP"):
        logger.info(f"[UPnP] Placeholder: abrir puerto {port}/{protocol} en el router.")
        # Aquí deberías implementar la lógica real usando miniupnpc o similar.
