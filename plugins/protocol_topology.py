from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class TopologyPlugin(BasePlugin):
    name = "Topology"

    def initialize(self, app_context):
        self.app_context = app_context

    def set_topology(self, mode):
        logger.info(f"[Topology] Placeholder: establecer topología {mode}.")
