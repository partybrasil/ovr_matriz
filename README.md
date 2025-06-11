# OVR-Matriz

OVR-Matriz es una plataforma modular, segura y extensible para transferencias de archivos, datos y control remoto, con soporte para múltiples protocolos y roles, interfaz gráfica (GUI) y de línea de comandos (CLI), y plugins para nuevas funciones.

## Funciones principales

- Transferencia de archivos y datos entre dispositivos (PC, Android, etc.).
- Control remoto (RDP/VNC, futuro).
- Soporte para múltiples protocolos: SSH/SFTP, FTP, SMB/CIFS, VPN (WireGuard/OpenVPN), ZeroTier, Proxys, WebRTC, MQTT, Android/Termux, y más.
- Gestión de roles y permisos (admin/user, RBAC editable).
- Cambio de protocolo en caliente (admin).
- Virtual LAN: crear, unir y gestionar redes virtuales tipo Hamachi/ZeroTier.
- Encabezado de estado siempre visible (GUI y CLI): conexión, rol, protocolo, seguridad, IPs, velocidad, etc.
- Plugins activables/desactivables en caliente.
- Seguridad robusta: autenticación JWT/OAuth2, handshake seguro, cifrado extremo a extremo (AES-256, ChaCha20, TLS 1.3).
- Logger avanzado, seguro y coloreado.
- Configuración dinámica (YAML/JSON), recarga sin reiniciar.
- **Barra de menús con accesos directos a todas las funciones y módulos de la app (GUI/CLI).**
- **Menú de configuraciones centralizado para modificar todos los parámetros de la app, módulos, plugins, conexiones, protocolos, cifrados, proxys, TLS y preferencias.**
- **Sistema de notificaciones automáticas (email y notificaciones live in-app).**
- **Soporte para múltiples idiomas (EN/ES/PT, pretensión inicial).**

## Próximas funciones a añadir

- Reportes personalizados.
- Integración con APIs externas.
- Soporte para múltiples idiomas.
- Control remoto avanzado (RDP/VNC).
- Más plugins y protocolos.

## Estructura del proyecto

```
ovr_matriz/
│
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── security.py
│   ├── roles.py
│   ├── logger.py
│   ├── plugin_manager.py
│   ├── protocols/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── utils.py
│   └── utils.py
│
├── plugins/
│   ├── __init__.py
│   ├── ssh_plugin.py
│   ├── ftp_plugin.py
│   ├── smb_plugin.py
│   ├── vpn_plugin.py
│   ├── zerotier_plugin.py
│   ├── proxy_plugin.py
│   ├── webrtc_plugin.py
│   ├── mqtt_plugin.py
│   ├── android_plugin.py
│   └── ...
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── routes/
│   ├── schemas/
│   └── dependencies.py
│
├── gui/
│   ├── __init__.py
│   ├── main.py
│   ├── themes/
│   ├── widgets/
│   ├── views/
│   ├── resources/
│   └── utils.py
│
├── cli/
│   ├── __init__.py
│   ├── main.py
│   ├── status_header.py
│   ├── commands/
│   └── utils.py
│
├── config/
│   ├── roles.yaml
│   └── app.yaml
│
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_plugins.py
│   ├── test_api.py
│   ├── test_gui.py
│   └── test_cli.py
│
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Protocolos soportados (plugins)

- SSH/SFTP (paramiko)
- FTP (pyftpdlib)
- SMB/CIFS (pysmb)
- VPN: WireGuard, OpenVPN
- Virtual LAN: ZeroTier, LAN virtual propia
- Proxys: SOCKS5, HTTP/HTTPS
- WebRTC (aiortc)
- MQTT (paho-mqtt)
- RDP/VNC (CLI, futuro)
- TLS/SSL (todas las conexiones)
- Android/Termux (plugin especial)
- Otros protocolos fácilmente integrables como plugins

## Seguridad

- Autenticación JWT, OAuth2, certificados X.509
- Handshake seguro (Diffie-Hellman, firmas digitales)
- Cifrado extremo a extremo (AES-256, ChaCha20, TLS 1.3)
- Roles y permisos RBAC, editable
- Logger seguro, cifrado, colores y tags
- Auditoría de acciones
- Protección contra ataques (rate limiting, validación, etc.)

## Multiplataforma

- Windows, Linux, Android (Termux)
- GUI (PySide6) y CLI (Rich) con encabezado de estado siempre visible

## Extensibilidad

- Sistema de plugins para protocolos y funciones
- API interna (gRPC/REST)
- Documentación OpenAPI/Swagger
- Testing con pytest

## Faltantes para estructura completa

- **Core**
  - Implementar la lógica real en: `config.py`, `security.py`, `logger.py`, `utils.py`, y los módulos de `protocols/`.
  - Completar la lógica de `roles.py`, `plugin_manager.py` y `state_header.py`.
  - Unificar el gestor de plugins (`plugin_manager.py`) y el auto-descubrimiento de plugins (`core/plugin_manager.py`).

- **Plugins**
  - Implementar todos los plugins listados en `plugins/` (actualmente solo hay esqueletos).
  - Definir la lógica real de conexión y operación para cada protocolo.
  - Añadir tests unitarios para cada plugin.

- **API**
  - Completar los endpoints en `main.py`, `routes/`, `schemas/`, `dependencies.py`.
  - Añadir autenticación, manejo de errores y documentación OpenAPI.

- **GUI**
  - Implementar la ventana principal y vistas en `main.py`, `main_window.py`, `widgets/`, `views/`.
  - Añadir lógica de interacción y encabezado de estado en tiempo real.
  - Implementar barra de menús con accesos directos a todas las funciones y módulos.
  - Añadir menú de configuraciones centralizado para modificar todos los parámetros y preferencias de la app, módulos, plugins, conexiones, protocolos, cifrados, proxys, TLS, idiomas, etc.
  - Integrar sistema de notificaciones automáticas (email y live in-app).
  - Añadir soporte para generación de reportes personalizados.
  - Integrar soporte para múltiples idiomas (EN/ES/PT).

- **CLI**
  - Completar comandos en `main.py`, `main_cli.py`, `status_header.py`, `commands/`.
  - Añadir lógica de interacción y encabezado de estado.

- **Configuración**
  - Definir y poblar los archivos en `config/` (`roles.yaml`, `app.yaml`, `settings.py`).

- **Testing**
  - Implementar tests funcionales y de integración en `tests/`.
  - Asegurar cobertura de plugins, core, CLI, GUI y API.

- **Integración**
  - Unir todos los módulos en los entrypoints (`main.py` y/o `app.py`) para que la app sea ejecutable y funcional.
  - Integrar el gestor de plugins con el core y la carga dinámica de plugins.

- **Documentación**
  - Completar la documentación de uso, instalación y desarrollo.
  - Añadir ejemplos de configuración y extensión de plugins.

> Consulta la estructura del proyecto y la documentación para detalles de cada módulo y archivo pendiente.

## Ejemplo de uso CLI

```bash
python main.py
# Selecciona "Gestor de plugins" para activar/desactivar plugins desde la CLI
```

## Ejemplo de uso GUI

- Accede al menú de configuración y abre el gestor de plugins para activar/desactivar plugins desde la interfaz gráfica.

## Testing

- Ejecuta los tests con:
```bash
pytest tests/
```