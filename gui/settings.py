from core.plugin_manager import CorePluginManager

def open_plugin_manager_window(app_context):
    # Lógica para abrir la ventana de gestión de plugins
    plugin_manager = CorePluginManager(app_context)
    print("Abriendo gestor de plugins...")
    for info in plugin_manager.get_all_plugin_info():
        print(f"- {info['name']} (Activo: {info['active']})")
    # Aquí se integraría la ventana real de gestión de plugins en la GUI

# En la configuración de la GUI, añadir acceso directo:
def settings_menu(app_context):
    # ...existing code...
    print("1. Configuración general")
    print("2. Parámetros avanzados")
    print("3. Gestor de plugins")  # Nuevo acceso directo
    # ...existing code...
    choice = input("Seleccione una opción: ")
    if choice == "3":
        open_plugin_manager_window(app_context)
    # ...existing code...