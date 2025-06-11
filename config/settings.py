import os

# Main settings and configuration
# Aquí se definen los parámetros globales de la app: protocolos habilitados, niveles de seguridad, rutas de archivos, etc.
# Incluye opciones para TLS, autenticación, MFA, logging, etc.
# Parámetros para menú de configuración centralizado.
# Parámetros para sistema de notificaciones (email, in-app).
# Parámetros para generación de reportes personalizados.
# Parámetros para integración con APIs externas.
# Parámetros para soporte de múltiples idiomas (EN/ES/PT).

class Settings:
    ENABLED_PROTOCOLS = [
        "ssh", "ftp", "smb", "vpn", "zerotier", "proxy", "webrtc", "mqtt", "android", "lan", "virtual_lan", "bluetooth", "directplay"
    ]
    SECURITY_LEVEL = "high"
    LOG_FILE = os.environ.get("OVR_LOG_FILE", "ovr_matriz.log")
    TLS_ENABLED = True
    AUTH_METHODS = ["jwt", "oauth2"]
    MFA_ENABLED = True
    NOTIFICATIONS = {
        "email": True,
        "in_app": True
    }
    REPORTS_ENABLED = True
    API_INTEGRATION = True
    SUPPORTED_LANGUAGES = ["en", "es", "pt"]
    DEFAULT_LANGUAGE = "es"

settings = Settings()
