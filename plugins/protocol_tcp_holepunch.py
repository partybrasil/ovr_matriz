from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class TcpHolePunchPlugin(BasePlugin):
    name = "TCP Hole Punching"

    def initialize(self, app_context):
        self.app_context = app_context

    def punch(self, peer_info):
        logger.info(f"[TCP Hole Punching] Placeholder: intentar hole punching con {peer_info}.")
