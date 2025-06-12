# Obsoleto: Usar core/plugin_manager.py para la gestión centralizada de plugins.*
# Este archivo se mantiene solo para compatibilidad temporal.*

from typing import List
from .base_plugin import BasePlugin
from .iplugin import IPlugin

class PluginManager:
    def __init__(self, app_context):
        self.plugins = []
        self.app_context = app_context

    def register(self, plugin: IPlugin):
        self.plugins.append(plugin)
        plugin.initialize(self.app_context)

    def get_plugins(self):
        return self.plugins
