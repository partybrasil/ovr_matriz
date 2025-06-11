from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class EoipPlugin(BasePlugin):
    name = "EoIP"

    def initialize(self, app_context):
        self.app_context = app_context

    def create_tunnel(self, tunnel_id, remote_ip):
        logger.info(f"[EoIP] Placeholder: crear túnel Ethernet-over-IP ID={tunnel_id} a {remote_ip}.")
        # Aquí deberías implementar la lógica real para crear un túnel EoIP.
