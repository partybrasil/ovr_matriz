from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class StarPlugin(BasePlugin):
    name = "Star"

    def initialize(self, app_context):
        self.app_context = app_context

    def join_star(self, hub_ip):
        logger.info(f"[Star] Placeholder: unir a hub central {hub_ip}.")
        # Aquí deberías implementar la lógica real para unirse a un hub central.

    def join(self, hub_id):
        logger.info(f"[Star] Placeholder: unir a hub central {hub_id}.")
        # Aquí deberías implementar la lógica real para unirse a un hub central.
