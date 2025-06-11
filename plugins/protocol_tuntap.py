from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class TunTapPlugin(BasePlugin):
    name = "TUN/TAP"

    def initialize(self, app_context):
        self.app_context = app_context

    def create_interface(self, name):
        logger.info(f"[TUN/TAP] Placeholder: crear interfaz virtual {name}.")
