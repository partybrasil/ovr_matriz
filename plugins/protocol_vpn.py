from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import subprocess
import shutil

class VpnPlugin(BasePlugin):
    name = "VPN"

    def initialize(self, app_context):
        self.app_context = app_context
        self.process = None
        self.connected = False

    def connect(self, config_path):
        if not has_permission(self.app_context.get("role", "user"), "use_vpn"):
            logger.warning("No permission to use VPN.")
            return
        if shutil.which("openvpn") is None:
            logger.error("[VPN] 'openvpn' no está instalado o no está en el PATH. Instálalo desde https://openvpn.net/community-downloads/")
            print("Para usar VPN necesitas instalar OpenVPN. Descárgalo de: https://openvpn.net/community-downloads/")
            return
        try:
            self.process = subprocess.Popen(["openvpn", "--config", config_path])
            self.connected = True
            logger.info(f"[VPN] Connected using config: {config_path}")
        except Exception as e:
            logger.error(f"[VPN] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if self.process:
            self.process.terminate()
        self.connected = False
        logger.info("[VPN] Disconnected")
