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
