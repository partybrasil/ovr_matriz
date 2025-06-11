from core.plugin_manager import CorePluginManager
from cli.connection_selector import select_connection_type
from cli.adapter_verifier import verify_adapters

def cli_plugin_manager(app_context):
    plugin_manager = CorePluginManager(app_context)
    print("Gestor de plugins CLI")
    for info in plugin_manager.get_all_plugin_info():
        print(f"- {info['name']} (Activo: {info['active']})")
    # Comandos básicos de ejemplo
    while True:
        cmd = input("Comando (activar <plugin>, desactivar <plugin>, salir): ")
        if cmd.startswith("activar "):
            name = cmd.split(" ", 1)[1]
            plugin_manager.activate_plugin(name)
            print(f"Plugin {name} activado.")
        elif cmd.startswith("desactivar "):
            name = cmd.split(" ", 1)[1]
            plugin_manager.deactivate_plugin(name)
            print(f"Plugin {name} desactivado.")
        elif cmd == "salir":
            break

def main_menu(app_context):
    # ...existing code...
    print("1. Ejecutar matriz")
    print("2. Configuración")
    print("3. Gestor de plugins")  # Nuevo acceso directo
    # ...existing code...
    choice = input("Seleccione una opción: ")
    if choice == "3":
        cli_plugin_manager(app_context)
    # ...existing code...

def main():
    print("Bienvenido al Gestor de Conexiones CLI")
    while True:
        print("\n1. Seleccionar tipo de conexión")
        print("2. Verificar adaptadores de red")
        print("3. Salir")
        opt = input("Opción: ")
        if opt == "1":
            select_connection_type()
        elif opt == "2":
            verify_adapters()
        elif opt == "3":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()