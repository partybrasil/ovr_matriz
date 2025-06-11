# Basic tests for core functionality

from core.plugin_manager import CorePluginManager
from plugins.sample_plugin import SamplePlugin

def test_plugin_registration():
    app_context = {"role": "admin"}
    manager = CorePluginManager(app_context)
    plugin = SamplePlugin()
    manager.register(plugin)
    assert plugin in manager.get_plugins()
    assert manager.get_plugin(plugin.name) == plugin
    plugin.activate()
    assert plugin.is_active()
    plugin.deactivate()
    assert not plugin.is_active()
