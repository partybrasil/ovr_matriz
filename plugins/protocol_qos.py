from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class QosPlugin(BasePlugin):
    name = "QoS"

    def initialize(self, app_context):
        self.app_context = app_context

    def set_priority(self, traffic_type, priority):
        logger.info(f"[QoS] Placeholder: establecer prioridad {priority} para {traffic_type}.")
