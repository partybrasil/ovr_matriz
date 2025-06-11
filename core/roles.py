# Roles and permissions schema
# Implementa control de acceso basado en roles (RBAC).
# Ejemplo: roles admin y user, cada uno con permisos específicos para funciones y protocolos.

ALL_PERMISSIONS = [
    "transfer_files",
    "view_status",
    "edit_matrix",
    "export_matrix",
    "apply_filters",
    "manage_users",
    "view_history",
    "undo_redo",
    "integrate_external_data",
    "configure_plugins",
    "view_reports",
    "generate_reports",
    "receive_notifications",
    "access_api",
    "change_settings",
    "multilanguage_support",
    "connect_directplay",
    "manage_roles",
    "delete_data",
    "import_matrix",
    "view_logs"
]

ROLES = {
    "admin": {
        "permissions": [
            # Admin tiene todos los permisos desglosados explícitamente
            "transfer_files",
            "view_status",
            "edit_matrix",
            "export_matrix",
            "apply_filters",
            "manage_users",
            "view_history",
            "undo_redo",
            "integrate_external_data",
            "configure_plugins",
            "view_reports",
            "generate_reports",
            "receive_notifications",
            "access_api",
            "change_settings",
            "multilanguage_support",
            "connect_directplay",
            "manage_roles",
            "delete_data",
            "import_matrix",
            "view_logs"
        ]
    },
    "user": {
        "permissions": [
            # Permisos mínimos para user
            "transfer_files",
            "view_status",
            "apply_filters",
            "export_matrix",
            "receive_notifications",
            "connect_directplay"  # Se asegura de que el usuario también tenga este permiso
        ]
    }
}

def has_permission(role, permission):
    perms = ROLES.get(role, {}).get("permissions", [])
    return permission in perms

def get_permissions(role):
    """Devuelve la lista de permisos para un rol."""
    return ROLES.get(role, {}).get("permissions", [])

import logging
import json
import os

USERS_FILE = os.path.join(os.path.dirname(__file__), "..", "config", "users.json")

# Diccionario de usuarios: username -> {"role": ..., "permissions": [...]}
USERS = {}

def load_users():
    global USERS
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                USERS.update(json.load(f))
        except Exception as e:
            logging.getLogger("ovr_matriz").error(f"[roles] Error cargando usuarios: {e}")

def save_users():
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(USERS, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logging.getLogger("ovr_matriz").error(f"[roles] Error guardando usuarios: {e}")

def create_user(username, role, custom_permissions=None, operator=None):
    """
    Crea un usuario nuevo con rol y permisos personalizados.
    Si custom_permissions es None, se asignan los permisos por defecto del rol.
    El operador es el usuario que realiza la acción (para logging).
    """
    if username in USERS:
        raise ValueError(f"El usuario '{username}' ya existe.")
    if role not in ROLES:
        raise ValueError(f"Rol '{role}' no válido.")
    perms = custom_permissions if custom_permissions is not None else get_permissions(role)
    USERS[username] = {
        "role": role,
        "permissions": perms
    }
    save_users()
    logger = logging.getLogger("ovr_matriz")
    logger.info(f"[roles] Usuario '{username}' creado con rol '{role}' por '{operator or 'system'}'.")

def delete_user(username, operator=None):
    """Elimina un usuario del sistema."""
    if username not in USERS:
        raise ValueError(f"Usuario '{username}' no existe.")
    del USERS[username]
    save_users()
    logger = logging.getLogger("ovr_matriz")
    logger.info(f"[roles] Usuario '{username}' eliminado por '{operator or 'system'}'.")

def get_user(username):
    """Devuelve la info del usuario o None si no existe."""
    return USERS.get(username)

def set_user_permissions(username, permissions, operator=None):
    """Actualiza los permisos de un usuario."""
    if username not in USERS:
        raise ValueError(f"Usuario '{username}' no existe.")
    USERS[username]["permissions"] = permissions
    save_users()
    logger = logging.getLogger("ovr_matriz")
    logger.info(f"[roles] Permisos de '{username}' actualizados por '{operator or 'system'}'.")

def set_user_role(username, role, operator=None):
    """Cambia el rol de un usuario y actualiza sus permisos por defecto."""
    if username not in USERS:
        raise ValueError(f"Usuario '{username}' no existe.")
    if role not in ROLES:
        raise ValueError(f"Rol '{role}' no válido.")
    USERS[username]["role"] = role
    USERS[username]["permissions"] = get_permissions(role)
    save_users()
    logger = logging.getLogger("ovr_matriz")
    logger.info(f"[roles] Rol de '{username}' cambiado a '{role}' por '{operator or 'system'}'.")

def list_users():
    """Devuelve la lista de usuarios registrados."""
    return list(USERS.keys())

# Cargar usuarios al importar el módulo
load_users()
