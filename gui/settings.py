from core.plugin_manager import CorePluginManager
from core.roles import create_user, ALL_PERMISSIONS, ROLES, list_users, delete_user

def open_plugin_manager_window(app_context):
    # Aquí se integraría la ventana real de gestión de plugins en la GUI
    print("Abriendo gestor de plugins (placeholder GUI*)...")
    plugin_manager = app_context.get("plugin_manager")
    for info in plugin_manager.get_all_plugin_info():
        print(f"- {info['name']} (Activo: {info['active']})")

def crear_usuario_interactivo_gui(operator="admin"):
    print("=== Crear nuevo usuario (GUI) ===")
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
        permisos = None
    try:
        create_user(username, role, custom_permissions=permisos, operator=operator)
        print(f"Usuario '{username}' creado exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

def eliminar_usuario_interactivo_gui(operator="admin"):
    print("=== Eliminar usuario (GUI) ===")
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

# En la configuración de la GUI, añadir acceso directo:
def settings_menu(app_context):
    # Aquí se integraría un diálogo real de configuración en la GUI
    print("Menú de configuración (placeholder GUI*)")
    print("1. Configuración general*")
    print("2. Parámetros avanzados*")
    print("3. Gestor de plugins*")
    print("4. Crear usuario nuevo")
    print("5. Listar usuarios")
    print("6. Eliminar usuario")
    choice = input("Seleccione una opción: ")
    if choice == "3":
        open_plugin_manager_window(app_context)
    elif choice == "4":
        crear_usuario_interactivo_gui(operator=app_context.get("current_user", "admin"))
    elif choice == "5":
        from core.roles import list_users
        print("Usuarios registrados:", ", ".join(list_users()))
    elif choice == "6":
        eliminar_usuario_interactivo_gui(operator=app_context.get("current_user", "admin"))