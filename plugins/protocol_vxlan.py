from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class VxlanPlugin(BasePlugin):
    name = "VXLAN"

    def initialize(self, app_context):
        self.app_context = app_context

    def create_tunnel(self, vni, remote_ip):
        logger.info(f"[VXLAN] Placeholder: crear túnel VXLAN VNI={vni} a {remote_ip}.")
