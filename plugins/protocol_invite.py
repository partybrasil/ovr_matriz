from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class InvitePlugin(BasePlugin):
    name = "Invite"

    def initialize(self, app_context):
        self.app_context = app_context

    def generate_code(self):
        logger.info("[Invite] Placeholder: generar código de invitación.")
        return "INVITE-CODE"
