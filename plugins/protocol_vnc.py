from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import socket

try:
    import vncdotool.api
except ImportError:
    vncdotool = None

class VncPlugin(BasePlugin):
    name = "VNC"

    def initialize(self, app_context):
        self.app_context = app_context
        self.client = None
        self.connected = False

    def connect(self, host, password, port=5900):
        if not has_permission(self.app_context.get("role", "user"), "use_vnc"):
            logger.warning("No permission to use VNC.")
            return
        if vncdotool is None:
            logger.error("[VNC] vncdotool no está instalado. Instálalo con: pip install vncdotool")
            print("Para usar VNC necesitas instalar vncdotool: pip install vncdotool")
            return
        try:
            self.client = vncdotool.api.connect(f"{host}::{port}", password=password)
            self.connected = True
            logger.info(f"[VNC] Connected to {host}:{port}")
        except Exception as e:
            logger.error(f"[VNC] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if self.client:
            try:
                self.client.close()
            except Exception:
                pass
        self.connected = False
        logger.info("[VNC] Disconnected")
