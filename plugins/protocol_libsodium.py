from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class LibsodiumPlugin(BasePlugin):
    name = "Libsodium"

    def initialize(self, app_context):
        self.app_context = app_context

    def encrypt(self, data, key):
        logger.info("[Libsodium] Placeholder: cifrando datos.")
        # Aquí deberías implementar la lógica real usando libsodium.

    def decrypt(self, data, key):
        logger.info("[Libsodium] Placeholder: descifrando datos.")
        # Aquí deberías implementar la lógica real usando libsodium.
