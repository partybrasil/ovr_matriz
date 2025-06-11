from core.plugin_manager import CorePluginManager
from cli.connection_selector import select_connection_type
from cli.adapter_verifier import verify_adapters
from core.roles import create_user, ALL_PERMISSIONS, list_users, delete_user, ROLES

def cli_plugin_manager(app_context):
    plugin_manager = app_context.get("plugin_manager")
    if not plugin_manager:
        plugin_manager = CorePluginManager(app_context)
        plugin_manager.auto_register_plugins()
        app_context["plugin_manager"] = plugin_manager
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

def crear_usuario_interactivo(operator="admin"):
    print("=== Crear nuevo usuario ===")
    username = input("Nombre de usuario: ")
    print("Roles disponibles:", ", ".join(ROLES.keys()))
    role = input("Rol (admin/user): ").strip()
    permisos = []
    print("¿Desea personalizar los permisos? (s/n)")
    if input().lower() == "s":
        for perm in ALL_PERMISSIONS:
            resp = input(f"¿Activar permiso '{perm}' para este usuario? (s/n): ")
            if resp.lower() == "s":
                permisos.append(perm)
    else:
        permisos = None  # Usar permisos por defecto del rol
    try:
        create_user(username, role, custom_permissions=permisos, operator=operator)
        print(f"Usuario '{username}' creado exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

def eliminar_usuario_interactivo(operator="admin"):
    print("=== Eliminar usuario ===")
    usuarios = list_users()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("Usuarios registrados:")
    for idx, u in enumerate(usuarios, 1):
        print(f"{idx}. {u}")
    try:
        sel = int(input("Seleccione el número del usuario a eliminar: ")) - 1
        if sel < 0 or sel >= len(usuarios):
            print("Selección inválida.")
            return
        username = usuarios[sel]
        confirm = input(f"¿Seguro que desea eliminar el usuario '{username}'? (s/n): ")
        if confirm.lower() == "s":
            delete_user(username, operator=operator)
            print(f"Usuario '{username}' eliminado.")
    except Exception as e:
        print(f"Error: {e}")

def main_menu(app_context):
    print("1. Ejecutar matriz")
    print("2. Configuración")
    print("3. Gestor de plugins")
    choice = input("Seleccione una opción: ")
    if choice == "3":
        cli_plugin_manager(app_context)

def main():
    app_context = {
        "role": "admin",
        "protocol": "none",
        "current_user": "admin"
    }
    plugin_manager = CorePluginManager(app_context)
    plugin_manager.auto_register_plugins()
    app_context["plugin_manager"] = plugin_manager
    print("Bienvenido al Gestor de Conexiones CLI")
    while True:
        print("\n1. Seleccionar tipo de conexión")
        print("2. Verificar adaptadores de red")
        print("3. Gestor de plugins")
        print("4. Crear usuario nuevo")
        print("5. Listar usuarios")
        print("6. Eliminar usuario")
        print("7. Salir")
        opt = input("Opción: ")
        if opt == "1":
            select_connection_type()
        elif opt == "2":
            verify_adapters()
        elif opt == "3":
            cli_plugin_manager(app_context)
        elif opt == "4":
            crear_usuario_interactivo(operator=app_context.get("current_user", "admin"))
        elif opt == "5":
            print("Usuarios registrados:", ", ".join(list_users()))
        elif opt == "6":
            eliminar_usuario_interactivo(operator=app_context.get("current_user", "admin"))
        elif opt == "7":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()