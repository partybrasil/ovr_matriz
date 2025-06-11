from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import paramiko

class SftpPlugin(BasePlugin):
    name = "SFTP"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, host, user, password=None, port=22):
        if not has_permission(self.app_context.get("role", "user"), "use_sftp"):
            logger.warning("No permission to use SFTP.")
            return
        try:
            transport = paramiko.Transport((host, port))
            transport.connect(username=user, password=password)
            self.sftp = paramiko.SFTPClient.from_transport(transport)
            self.connected = True
            logger.info(f"[SFTP] Connected to {user}@{host}")
        except Exception as e:
            logger.error(f"[SFTP] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if hasattr(self, "sftp") and self.sftp:
            self.sftp.close()
        self.connected = False
        logger.info("[SFTP] Disconnected")
