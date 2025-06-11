from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class ProxyPlugin(BasePlugin):
    name = "Proxy"

    def initialize(self, app_context):
        self.app_context = app_context
        self.proxies = {
            "SOCKS4": [],
            "SOCKS5": [],
            "HTTP": [],
            "HTTPS": []
        }

    def load_proxies_from_txt(self, filepath):
        """
        Formato esperado:
        Cada línea: tipo_proxy://usuario:contraseña@host:puerto
        Ejemplo:
        socks5://user:pass@127.0.0.1:1080
        http://127.0.0.1:8080
        https://user:pass@proxy.example.com:443
        socks4://127.0.0.1:9050
        """
        try:
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if line.lower().startswith("socks5://"):
                        self.proxies["SOCKS5"].append(line)
                    elif line.lower().startswith("socks4://"):
                        self.proxies["SOCKS4"].append(line)
                    elif line.lower().startswith("http://"):
                        self.proxies["HTTP"].append(line)
                    elif line.lower().startswith("https://"):
                        self.proxies["HTTPS"].append(line)
            logger.info(f"[Proxy] Proxies cargados desde {filepath}")
        except Exception as e:
            logger.error(f"[Proxy] Error cargando proxies: {e}")

    def get_proxies(self, proxy_type=None):
        if proxy_type:
            return self.proxies.get(proxy_type.upper(), [])
        return self.proxies
