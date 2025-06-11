from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class LobbyPlugin(BasePlugin):
    name = "Lobby"

    def initialize(self, app_context):
        self.app_context = app_context

    def create_lobby(self):
        logger.info("[Lobby] Placeholder: crear lobby central.")
