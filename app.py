# ELIMINAR ESTE ARCHIVO - La entrada principal es main.py y la gestión de plugins está centralizada.

from plugins.plugin_manager import PluginManager
from plugins.directplay_plugin import DirectPlayPlugin

app_context = {
    # ...existing code...
}

plugin_manager = PluginManager(app_context)
plugin_manager.register(DirectPlayPlugin())