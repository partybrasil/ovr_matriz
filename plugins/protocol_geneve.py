from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class GenevePlugin(BasePlugin):
    name = "GENEVE"

    def initialize(self, app_context):
        self.app_context = app_context

    def create_tunnel(self, vni, remote_ip):
        logger.info(f"[GENEVE] Placeholder: crear túnel GENEVE VNI={vni} a {remote_ip}.")
