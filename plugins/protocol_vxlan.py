from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission
# Añade import para pyroute2 si estás en Linux
try:
    from pyroute2 import IPRoute
except ImportError:
    IPRoute = None

class VxlanPlugin(BasePlugin):
    name = "VXLAN"

    def initialize(self, app_context):
        self.app_context = app_context

    def create_tunnel(self, vni, remote_ip):
        # Lógica real para crear túnel VXLAN en Linux
        if IPRoute is None:
            logger.error("[VXLAN] pyroute2 no está instalado. Instala pyroute2 para soporte real.")
            return False
        ipr = IPRoute()
        vxlan_name = f"vxlan{vni}"
        try:
            ipr.link("add", ifname=vxlan_name, kind="vxlan", vxlan_id=int(vni), remote=remote_ip)
            ipr.link("set", ifname=vxlan_name, state="up")
            logger.info(f"[VXLAN] Túnel VXLAN {vxlan_name} creado hacia {remote_ip}.")
            return True
        except Exception as e:
            logger.error(f"[VXLAN] Error creando túnel: {e}")
            return False
