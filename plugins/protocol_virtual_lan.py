# Virtual LAN protocol plugin

from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
import subprocess
import shutil

class VirtualLanPlugin(BasePlugin):
    name = "VirtualLAN"

    def initialize(self, app_context):
        # Inicialización del plugin de red virtual
        self.app_context = app_context
        self.networks = []

    def create_network(self, network_id):
        if not has_permission(self.app_context.get("role", "user"), "create_virtual_lan"):
            logger.warning("No permission to create virtual LAN.")
            return
        if shutil.which("zerotier-cli") is None:
            logger.error("[VirtualLAN] 'zerotier-cli' no está instalado o no está en el PATH. Instálalo desde https://www.zerotier.com/download/")
            print("Para usar redes virtuales necesitas instalar ZeroTier. Descárgalo de: https://www.zerotier.com/download/")
            return
        try:
            subprocess.check_call(["zerotier-cli", "join", network_id])
            self.networks.append(network_id)
            logger.info(f"[VirtualLAN] Network '{network_id}' joined")
        except Exception as e:
            logger.error(f"[VirtualLAN] Failed to join network: {e}")

    def list_networks(self):
        if shutil.which("zerotier-cli") is None:
            logger.error("[VirtualLAN] 'zerotier-cli' no está instalado o no está en el PATH. Instálalo desde https://www.zerotier.com/download/")
            print("Para usar redes virtuales necesitas instalar ZeroTier. Descárgalo de: https://www.zerotier.com/download/")
            return []
        try:
            output = subprocess.check_output(["zerotier-cli", "listnetworks"]).decode()
            logger.info(f"[VirtualLAN] Networks: {output}")
            return output
        except Exception as e:
            logger.error(f"[VirtualLAN] Failed to list networks: {e}")
            return []
