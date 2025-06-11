from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import subprocess
import sys
import shutil

class RdpPlugin(BasePlugin):
    name = "RDP"

    def initialize(self, app_context):
        self.app_context = app_context
        self.process = None
        self.connected = False

    def connect(self, host, user, password=None):
        if not has_permission(self.app_context.get("role", "user"), "use_rdp"):
            logger.warning("No permission to use RDP.")
            return
        try:
            if sys.platform.startswith("win"):
                if shutil.which("mstsc") is None:
                    logger.error("[RDP] 'mstsc' no está instalado o no está en el PATH. Es parte de Windows, busca 'Conexión a Escritorio Remoto'.")
                    print("Para usar RDP en Windows necesitas 'mstsc' (Conexión a Escritorio Remoto). Busca en el menú de inicio o instala las herramientas de escritorio remoto de Windows.")
                    return
                cmd = ["mstsc", "/v:{}".format(host)]
                self.process = subprocess.Popen(cmd)
            else:
                if shutil.which("xfreerdp") is None:
                    logger.error("[RDP] 'xfreerdp' no está instalado o no está en el PATH. Instálalo con tu gestor de paquetes, por ejemplo: sudo apt install freerdp2-x11")
                    print("Para usar RDP en Linux necesitas instalar xfreerdp. Ejemplo: sudo apt install freerdp2-x11")
                    return
                cmd = ["xfreerdp", f"/u:{user}", f"/p:{password or ''}", f"/v:{host}"]
                self.process = subprocess.Popen(cmd)
            self.connected = True
            logger.info(f"[RDP] Connected to {host} as {user}")
        except Exception as e:
            logger.error(f"[RDP] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if self.process:
            self.process.terminate()
        self.connected = False
        logger.info("[RDP] Disconnected")
