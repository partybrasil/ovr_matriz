from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import shutil
import subprocess

class WireGuardPlugin(BasePlugin):
    name = "WireGuard"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, config_path):
        if not has_permission(self.app_context.get("role", "user"), "use_wireguard"):
            logger.warning("No permission to use WireGuard.")
            return
        if shutil.which("wg-quick") is None:
            logger.error("[WireGuard] 'wg-quick' no está instalado. Instálalo desde https://www.wireguard.com/install/")
            print("Para usar WireGuard necesitas instalar wg-quick. Descárgalo de: https://www.wireguard.com/install/")
            return
        try:
            subprocess.check_call(["wg-quick", "up", config_path])
            self.connected = True
            logger.info(f"[WireGuard] Connected using config: {config_path}")
        except Exception as e:
            logger.error(f"[WireGuard] Connection failed: {e}")
            self.connected = False

    def disconnect(self, config_path):
        if shutil.which("wg-quick") is None:
            return
        try:
            subprocess.check_call(["wg-quick", "down", config_path])
        except Exception:
            pass
        self.connected = False
        logger.info("[WireGuard] Disconnected")
