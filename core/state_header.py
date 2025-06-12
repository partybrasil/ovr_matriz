import socket
import psutil
import requests

# State header for GUI and CLI (real-time updates)
class StateHeader:
    def __init__(self, app_context):
        self.app_context = app_context

    def get_host_name(self):
        return socket.gethostname()

    def get_active_adapter(self):
        # Selecciona el primer adaptador con IP válida (puedes mejorar la lógica)
        adapters = psutil.net_if_addrs()
        for name, addrs in adapters.items():
            for addr in addrs:
                if addr.family.name == "AF_INET" and not addr.address.startswith("169.254"):
                    return name, addr.address
        return "Desconocido", "0.0.0.0"

    def get_public_ip(self):
        try:
            return requests.get("https://api.ipify.org").text
        except Exception:
            return "Desconocida"

    def get_connection_status(self):
        # Placeholder: puedes mejorar con lógica real
        return self.app_context.get("estado", "Conectado")

    def get_network_quality(self):
        # Placeholder: lógica real de calidad de red
        return self.app_context.get("calidad", "Buena")

    def get_speed(self):
        # Placeholder: lógica real de velocidad
        return self.app_context.get("velocidad", {"download": "0 Mbps", "upload": "0 Mbps"})

    def get_dest_info(self):
        # Placeholder: lógica real para obtener info del destino
        return self.app_context.get("destino", {
            "host": "Remoto",
            "adapter": "Desconocido",
            "status": "Desconocido",
            "ip_publica": "Desconocida",
            "ip_privada": "Desconocida"
        })

    def get_status(self):
        host = self.get_host_name()
        adapter, ip_priv = self.get_active_adapter()
        ip_pub = self.get_public_ip()
        protocolo = self.app_context.get("protocol", "none")
        estado = self.get_connection_status()
        calidad = self.get_network_quality()
        velocidad = self.get_speed()
        destino = self.get_dest_info()
        return {
            "yo": host,
            "red": f"{adapter} | {ip_priv} | Pública: {ip_pub}",
            "protocolo": protocolo,
            "estado": f"{estado} | Conflictos: {self.app_context.get('conflictos', 'Ninguno')} | Calidad: {calidad} | Vel: ↓{velocidad['download']} ↑{velocidad['upload']}",
            "destino": destino["host"],
            "red_destino": f"{destino['adapter']} | {destino['ip_privada']} | Pública: {destino['ip_publica']} | Estado: {destino['status']}"
        }
