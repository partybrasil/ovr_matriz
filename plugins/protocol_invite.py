from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class InvitePlugin(BasePlugin):
    name = "Invite"

    def initialize(self, app_context):
        self.app_context = app_context

    def generate_code(self, session_id):
        logger.info(f"[Invite] Placeholder: generar código de invitación para sesión {session_id}.")
        # Aquí deberías implementar la lógica real para generar códigos de invitación.
