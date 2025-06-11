from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import paramiko

class SshPlugin(BasePlugin):
    name = "SSH"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, host, user, password=None, port=22):
        if not has_permission(self.app_context.get("role", "user"), "use_ssh"):
            logger.warning("No permission to use SSH.")
            return
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=host, username=user, password=password, port=port)
            self.connected = True
            logger.info(f"[SSH] Connected to {user}@{host}")
        except Exception as e:
            logger.error(f"[SSH] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if hasattr(self, "ssh_client") and self.ssh_client:
            self.ssh_client.close()
        self.connected = False
        logger.info("[SSH] Disconnected")
