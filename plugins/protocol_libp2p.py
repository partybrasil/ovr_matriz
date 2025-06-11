from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class Libp2pPlugin(BasePlugin):
    name = "libp2p"

    def initialize(self, app_context):
        self.app_context = app_context

    def connect(self, peer_id):
        logger.info(f"[libp2p] Placeholder: conectar a peer {peer_id}.")
