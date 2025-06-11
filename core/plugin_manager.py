# Plugin manager for protocol plugins
# Arquitectura modular: cada protocolo (VPN, SSH, FTP, SFTP, WebDAV, SMB, RDP, VNC, etc.) es un plugin independiente.
# Para agregar un nuevo protocolo, crea un archivo en plugins/ y registra el plugin aquí.
# Ejemplo de protocolos recomendados: WireGuard, ZeroTier, SFTP, SCP, WebDAV, SMB, RDP, VNC, QUIC, MQTT, gRPC, Tor, etc.

import importlib
import pkgutil
from plugins.base_plugin import BasePlugin

class CorePluginManager:
    def __init__(self, app_context):
        self.plugins = []
        self.app_context = app_context
        self.active_plugins = {}

    def auto_register_plugins(self):
        """
        Descubre y registra automáticamente todos los plugins válidos en plugins/.
        """
        import plugins
        for _, modname, ispkg in pkgutil.iter_modules(plugins.__path__):
            if not ispkg and not modname.startswith("__") and not modname.endswith(".ts"):
                try:
                    module = importlib.import_module(f"plugins.{modname}")
                    for attr in dir(module):
                        obj = getattr(module, attr)
                        if isinstance(obj, type) and issubclass(obj, BasePlugin) and obj is not BasePlugin:
                            self.register(obj())
                except Exception as e:
                    print(f"Error cargando plugin {modname}: {e}")

    def reload_plugins(self):
        """Recarga todos los plugins dinámicamente."""
        self.plugins.clear()
        self.active_plugins.clear()
        self.auto_register_plugins()

    def register(self, plugin: BasePlugin):
        self.plugins.append(plugin)
        plugin.initialize(self.app_context)
        self.active_plugins[plugin.name] = plugin

    def get_plugins(self):
        return self.plugins

    def get_plugin(self, name):
        return self.active_plugins.get(name)

    def activate_plugin(self, name):
        plugin = self.get_plugin(name)
        if plugin:
            plugin.activate()

    def deactivate_plugin(self, name):
        plugin = self.get_plugin(name)
        if plugin:
            plugin.deactivate()

    def install_plugin(self, plugin_cls):
        """Instala y registra un nuevo plugin dinámicamente."""
        plugin = plugin_cls()
        self.register(plugin)
        return plugin

    def uninstall_plugin(self, name):
        """Desinstala un plugin por nombre."""
        plugin = self.active_plugins.pop(name, None)
        if plugin and plugin in self.plugins:
            self.plugins.remove(plugin)
        return plugin

    def configure_plugin(self, name, **kwargs):
        """Configura un plugin pasando parámetros arbitrarios."""
        plugin = self.get_plugin(name)
        if plugin and hasattr(plugin, "configure"):
            plugin.configure(**kwargs)
            return True
        return False

    def modify_plugin(self, name, **kwargs):
        """Modifica propiedades del plugin en caliente."""
        plugin = self.get_plugin(name)
        if plugin:
            for k, v in kwargs.items():
                setattr(plugin, k, v)
            return True
        return False

    def list_plugins(self, active_only=False):
        """Lista todos los plugins o solo los activos."""
        if active_only:
            return [p for p in self.plugins if p.is_active()]
        return self.plugins

    # Métodos para integración con CLI/GUI
    def get_plugin_info(self, name):
        plugin = self.get_plugin(name)
        if plugin:
            return {
                "name": plugin.name,
                "active": plugin.is_active(),
                "type": type(plugin).__name__,
                "configurable": hasattr(plugin, "configure"),
            }
        return None

    def get_all_plugin_info(self):
        return [self.get_plugin_info(p.name) for p in self.plugins]

# El sistema de auto_register_plugins ya detectará DirectPlayPlugin si está en plugins/
