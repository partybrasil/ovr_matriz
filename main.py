# Main entry point for OVR-Matriz

from core.plugin_manager import CorePluginManager
from core.logger import logger
from core.roles import has_permission
from config.settings import settings

def main():
    # Contexto global de la app
    app_context = {
        "role": "admin",
        "protocol": "none",
        "settings": settings
    }

    # Inicializa el gestor de plugins del core (auto-descubrimiento)
    plugin_manager = CorePluginManager(app_context)
    plugin_manager.auto_register_plugins()

    # Ejemplo: activar y usar un plugin solo si el rol tiene permiso
    plugin_name = "Bluetooth"
    if has_permission(app_context["role"], "use_bluetooth"):
        bluetooth = plugin_manager.get_plugin(plugin_name)
        if bluetooth:
            bluetooth.activate()
            bluetooth.connect("Device_XYZ")
            logger.info(f"{plugin_name} plugin activated and connected.")
        else:
            logger.warning(f"{plugin_name} plugin not found.")
    else:
        logger.warning(f"Role {app_context['role']} does not have permission to use {plugin_name}.")

    # Aquí puedes iniciar la CLI o GUI según argumentos
    # Por ejemplo:
    # from cli.main_cli import start_cli
    # from gui.main_window import start_gui
    # start_cli(app_context)
    # start_gui(app_context)

if __name__ == "__main__":
    main()
