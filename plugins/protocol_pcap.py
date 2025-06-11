from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class PcapPlugin(BasePlugin):
    name = "Pcap"

    def initialize(self, app_context):
        self.app_context = app_context

    def capture(self, interface):
        logger.info(f"[Pcap] Placeholder: capturando paquetes en {interface}.")
        # Aquí deberías implementar la lógica real usando pcapy, scapy, o pyshark.
