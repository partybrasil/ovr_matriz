from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
from smbprotocol.connection import Connection
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
import uuid

class SmbPlugin(BasePlugin):
    name = "SMB"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, share, user, password=None, server=None):
        if not has_permission(self.app_context.get("role", "user"), "use_smb"):
            logger.warning("No permission to use SMB.")
            return
        try:
            self.connection = Connection(uuid.uuid4(), server, 445)
            self.connection.connect()
            self.session = Session(self.connection, user, password)
            self.session.connect()
            self.tree = TreeConnect(self.session, share)
            self.tree.connect()
            self.connected = True
            logger.info(f"[SMB] Connected to {share} as {user}")
        except Exception as e:
            logger.error(f"[SMB] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if hasattr(self, "tree") and self.tree:
            self.tree.disconnect()
        if hasattr(self, "session") and self.session:
            self.session.disconnect()
        if hasattr(self, "connection") and self.connection:
            self.connection.disconnect()
        self.connected = False
        logger.info("[SMB] Disconnected")
