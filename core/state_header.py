# State header for GUI and CLI (real-time updates)

class StateHeader:
    def __init__(self, app_context):
        self.app_context = app_context

    def get_status(self):
        # Devuelve un dict con el estado actual (conexión, rol, protocolo, etc.)
        return {
            "connection": "online",
            "role": self.app_context.get("role", "user"),
            "protocol": self.app_context.get("protocol", "none"),
            # Agrega más campos según sea necesario
        }
