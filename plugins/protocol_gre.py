from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class GrePlugin(BasePlugin):
    name = "GRE"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, remote_ip):
        logger.info(f"[GRE] Placeholder: conectar túnel GRE a {remote_ip}.")
        self.connected = True

    def disconnect(self):
        self.connected = False
        logger.info("[GRE] Disconnected")
