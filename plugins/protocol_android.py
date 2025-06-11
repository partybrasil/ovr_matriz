from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import subprocess
import shutil

class AndroidPlugin(BasePlugin):
    name = "Android"

    def initialize(self, app_context):
        self.app_context = app_context
        self.connected = False

    def connect(self, device):
        if not has_permission(self.app_context.get("role", "user"), "use_android"):
            logger.warning("No permission to use Android plugin.")
            return
        if shutil.which("adb") is None:
            logger.error("[Android] 'adb' no está instalado o no está en el PATH. Instálalo desde https://developer.android.com/tools/releases/platform-tools")
            print("Para usar el plugin Android necesitas instalar ADB. Descárgalo de: https://developer.android.com/tools/releases/platform-tools")
            return
        try:
            subprocess.check_call(["adb", "connect", device])
            self.connected = True
            logger.info(f"[Android] Connected to {device}")
        except Exception as e:
            logger.error(f"[Android] Connection failed: {e}")
            self.connected = False

    def disconnect(self, device=None):
        if shutil.which("adb") is None:
            logger.error("[Android] 'adb' no está instalado o no está en el PATH. Instálalo desde https://developer.android.com/tools/releases/platform-tools")
            print("Para usar el plugin Android necesitas instalar ADB. Descárgalo de: https://developer.android.com/tools/releases/platform-tools")
            return
        try:
            if device:
                subprocess.check_call(["adb", "disconnect", device])
            else:
                subprocess.check_call(["adb", "disconnect"])
        except Exception:
            pass
        self.connected = False
        logger.info("[Android] Disconnected")