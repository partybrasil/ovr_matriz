from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class QuicPlugin(BasePlugin):
    name = "QUIC"

    def initialize(self, app_context):
        self.app_context = app_context

    def connect(self, host, port):
        logger.info(f"[QUIC] Placeholder: conectar a {host}:{port} usando QUIC.")
