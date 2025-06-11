from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

try:
    import bluetooth
except ImportError:
    bluetooth = None

class BluetoothPlugin(BasePlugin):
    name = "Bluetooth"

    def initialize(self, app_context):
        self.app_context = app_context
        self.sock = None
        self.connected = False

    def connect(self, device_addr, port=1):
        if not has_permission(self.app_context.get("role", "user"), "use_bluetooth"):
            logger.warning("No permission to use Bluetooth.")
            return
        if bluetooth is None:
            logger.error("[Bluetooth] pybluez-pypi no está instalado. Instálalo con: pip install pybluez-pypi")
            print("Para usar Bluetooth necesitas instalar pybluez-pypi: pip install pybluez-pypi")
            return
        try:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((device_addr, port))
            self.connected = True
            logger.info(f"[Bluetooth] Connected to {device_addr}")
        except Exception as e:
            logger.error(f"[Bluetooth] Connection failed: {e}")
            self.connected = False

    def disconnect(self):
        if self.sock:
            try:
                self.sock.close()
            except Exception:
                pass
        self.connected = False
        logger.info("[Bluetooth] Disconnected")