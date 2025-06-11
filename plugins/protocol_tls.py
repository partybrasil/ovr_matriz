from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class TlsPlugin(BasePlugin):
    name = "TLS"

    def initialize(self, app_context):
        self.app_context = app_context

    def secure_connection(self, connection):
        logger.info("[TLS] Placeholder: asegurar conexión con TLS.")
