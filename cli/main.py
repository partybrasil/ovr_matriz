from core.plugin_manager import CorePluginManager
from cli.connection_selector import select_connection_type
from cli.adapter_verifier import verify_adapters
from core.roles import create_user, ALL_PERMISSIONS, list_users, delete_user, ROLES
from core.state_header import StateHeader
from rich.console import Console
from rich.table import Table

def cli_plugin_manager(app_context):
    plugin_manager = app_context.get("plugin_manager")
    if not plugin_manager:
        plugin_manager = CorePluginManager(app_context)
        plugin_manager.auto_register_plugins()
        app_context["plugin_manager"] = plugin_manager
    while True:
        print("\n=== Gestor de Plugins ===")
        plugins = plugin_manager.get_all_plugin_info()
        for idx, info in enumerate(plugins, 1):
            estado = "Activo" if info["active"] else "Inactivo"
            print(f"{idx}. {info['name']} [{estado}]")
        print("a) Activar plugin")
        print("d) Desactivar plugin")
        print("r) Recargar plugins")
        print("q) Volver")
        cmd = input("Opción: ").strip().lower()
        if cmd == "a":
            sel = input("Nombre del plugin a activar: ")
            plugin_manager.activate_plugin(sel)
            print(f"Plugin {sel} activado.")
        elif cmd == "d":
            sel = input("Nombre del plugin a desactivar: ")
            plugin_manager.deactivate_plugin(sel)
            print(f"Plugin {sel} desactivado.")
        elif cmd == "r":
            plugin_manager.reload_plugins()
            print("Plugins recargados.")
        elif cmd == "q":
            break

def cli_config_menu(app_context):
    print("\n=== Menú de Configuración ===")
    print("1. Configuración general")
    print("2. Parámetros avanzados")
    print("3. Preferencias de usuario")
    print("4. Idioma")
    print("5. Seguridad")
    print("6. Volver")
    opt = input("Seleccione una opción: ")
    if opt == "6":
        return
    print("Funcionalidad de configuración aún no implementada (placeholder).")

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

def mostrar_encabezado(app_context):
    header = StateHeader(app_context).get_status()
    table = Table(show_header=False, box=None)
    table.add_row(f"[bold]YO:[/bold] {header['yo']}")
    table.add_row(f"[bold]RED:[/bold] {header['red']}")
    table.add_row(f"[bold]PROTOCOLO:[/bold] {header['protocolo']}")
    table.add_row(f"[bold]ESTADO:[/bold] {header['estado']}")
    table.add_row(f"[bold]DESTINO:[/bold] {header['destino']}")
    table.add_row(f"[bold]RED DESTINO:[/bold] {header['red_destino']}")
    console = Console()
    console.clear()
    console.print(table)
    print("-" * 60)

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
        print("4. Menú de configuración")
        print("5. Crear usuario nuevo")
        print("6. Listar usuarios")
        print("7. Eliminar usuario")
        print("8. Salir")
        opt = input("Opción: ")
        if opt == "1":
            select_connection_type()
        elif opt == "2":
            verify_adapters()
        elif opt == "3":
            cli_plugin_manager(app_context)
        elif opt == "4":
            cli_config_menu(app_context)
        elif opt == "5":
            crear_usuario_interactivo(operator=app_context.get("current_user", "admin"))
        elif opt == "6":
            print("Usuarios registrados:", ", ".join(list_users()))
        elif opt == "7":
            eliminar_usuario_interactivo(operator=app_context.get("current_user", "admin"))
        elif opt == "8":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()