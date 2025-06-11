from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class UdpHolePunchPlugin(BasePlugin):
    name = "UDP Hole Punching"

    def initialize(self, app_context):
        self.app_context = app_context

    def punch(self, peer_info):
        logger.info(f"[UDP Hole Punching] Placeholder: intentar hole punching con {peer_info}.")
