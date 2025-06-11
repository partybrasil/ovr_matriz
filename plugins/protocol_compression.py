from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class CompressionPlugin(BasePlugin):
    name = "Compression"

    def initialize(self, app_context):
        self.app_context = app_context

    def compress(self, data):
        logger.info("[Compression] Placeholder: comprimir datos.")
        return data

    def decompress(self, data):
        logger.info("[Compression] Placeholder: descomprimir datos.")
        return data
