from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
from webdav3.client import Client

class WebdavPlugin(BasePlugin):
    name = "WebDAV"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, url, user, password=None):
        if not has_permission(self.app_context.get("role", "user"), "use_webdav"):
            logger.warning("No permission to use WebDAV.")
            return
        try:
            options = {
                'webdav_hostname': url,
                'webdav_login': user,
                'webdav_password': password
            }
            self.client = Client(options)
            # Probar conexión
            self.client.list("/")
            self.connected = True
            logger.info(f"[WebDAV] Connected to {url} as {user}")
        except Exception as e:
            logger.error(f"[WebDAV] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        self.connected = False
        logger.info("[WebDAV] Disconnected")
