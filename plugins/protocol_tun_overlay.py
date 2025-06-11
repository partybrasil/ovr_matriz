from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class TunOverlayPlugin(BasePlugin):
    name = "TUN Overlay"

    def initialize(self, app_context):
        self.app_context = app_context

    def create_overlay(self, name):
        logger.info(f"[TUN Overlay] Placeholder: crear overlay TUN {name}.")
        # Aquí deberías implementar la lógica real para overlays TUN.
