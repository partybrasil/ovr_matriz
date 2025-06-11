from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class LibsodiumPlugin(BasePlugin):
    name = "Libsodium"

    def initialize(self, app_context):
        self.app_context = app_context

    def encrypt(self, data):
        logger.info("[Libsodium] Placeholder: cifrar datos.")
        return data

    def decrypt(self, data):
        logger.info("[Libsodium] Placeholder: descifrar datos.")
        return data
