from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class NatPmpPlugin(BasePlugin):
    name = "NAT-PMP"

    def initialize(self, app_context):
        self.app_context = app_context

    def open_port(self, port):
        logger.info(f"[NAT-PMP] Placeholder: abrir puerto {port} usando NAT-PMP.")
