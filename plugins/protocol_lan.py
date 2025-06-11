# LAN protocol plugin

from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

try:
    import nmap
except ImportError:
    nmap = None

class LanPlugin(BasePlugin):
    name = "LAN"

    def initialize(self, app_context):
        # Inicialización del plugin de LAN
        self.app_context = app_context
        self.devices = []

    def scan_devices(self, subnet="192.168.1.0/24"):
        if not has_permission(self.app_context.get("role", "user"), "scan_lan"):
            logger.warning("No permission to scan LAN devices.")
            return []
        if nmap is None:
            logger.error("[LAN] python-nmap no está instalado. Instálalo con: pip install python-nmap")
            print("Para escanear la LAN necesitas instalar python-nmap: pip install python-nmap")
            return []
        import shutil
        if shutil.which("nmap") is None:
            logger.error("[LAN] 'nmap' no está instalado o no está en el PATH. Instálalo desde https://nmap.org/download.html")
            print("Para escanear la LAN necesitas instalar nmap. Descárgalo de: https://nmap.org/download.html")
            return []
        try:
            nm = nmap.PortScanner()
            nm.scan(hosts=subnet, arguments='-sn')
            self.devices = [host for host in nm.all_hosts()]
            logger.info(f"[LAN] Devices found: {self.devices}")
            return self.devices
        except Exception as e:
            logger.error(f"[LAN] Scan failed: {e}")
            return []
