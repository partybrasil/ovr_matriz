from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class AuthPlugin(BasePlugin):
    name = "Auth"

    def initialize(self, app_context):
        self.app_context = app_context

    def authenticate(self, username, password):
        logger.info("[Auth] Placeholder: autenticando usuario.")
        # Aquí deberías implementar la lógica real de autenticación.
