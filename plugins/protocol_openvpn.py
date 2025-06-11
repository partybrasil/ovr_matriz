from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import shutil
import subprocess

class OpenVpnPlugin(BasePlugin):
    name = "OpenVPN"

    def initialize(self, app_context):
        self.app_context = app_context
        self.process = None
        self.connected = False

    def connect(self, config_path):
        if not has_permission(self.app_context.get("role", "user"), "use_openvpn"):
            logger.warning("No permission to use OpenVPN.")
            return
        if shutil.which("openvpn") is None:
            logger.error("[OpenVPN] 'openvpn' no está instalado. Instálalo desde https://openvpn.net/community-downloads/")
            print("Para usar OpenVPN necesitas instalarlo. Descárgalo de: https://openvpn.net/community-downloads/")
            return
        try:
            self.process = subprocess.Popen(["openvpn", "--config", config_path])
            self.connected = True
            logger.info(f"[OpenVPN] Connected using config: {config_path}")
        except Exception as e:
            logger.error(f"[OpenVPN] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if self.process:
            self.process.terminate()
        self.connected = False
        logger.info("[OpenVPN] Disconnected")
