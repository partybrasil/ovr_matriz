# OVR-Matriz

Plataforma modular, segura y extensible para transferencias de archivos, datos y control remoto, con soporte multiplataforma (Windows, Linux, Android/Termux), GUI y CLI, y plugins para nuevos protocolos y funciones.

## Funciones principales

- Transferencia de archivos/datos y control remoto.
- Soporte para múltiples protocolos (SSH/SFTP, FTP, SMB, VPN, ZeroTier, Proxys, WebRTC, MQTT, Android, etc.).
- Gestión de roles y permisos (admin/user, RBAC editable).
- Cambio de protocolo en caliente (admin).
- Virtual LAN: crear, unir y gestionar redes virtuales.
- Encabezado de estado siempre visible (GUI y CLI).
- Plugins activables/desactivables en caliente.
- Seguridad robusta: autenticación, handshake seguro, cifrado extremo a extremo.
- Logger avanzado, seguro y coloreado.
- Configuración dinámica (YAML/JSON).
- Multiplataforma: Windows, Linux, Android (Termux).
- Testing y documentación listos para CI/CD.
- **Barra de menús y menú de configuraciones centralizado (GUI/CLI).**
- **Sistema de notificaciones automáticas (email y live in-app).**
- **Soporte para múltiples idiomas (EN/ES/PT, inicial).**

## Próximas funciones a añadir

- Reportes personalizados.
- Integración con APIs externas.
- Soporte para múltiples idiomas.
- Control remoto avanzado (RDP/VNC).
- Más plugins y protocolos.

## Estructura del proyecto

Ver README principal para estructura detallada.

## Protocolos soportados (plugins)

- SSH/SFTP
- FTP
- SMB/CIFS
- VPN: WireGuard, OpenVPN
- Virtual LAN: ZeroTier, LAN virtual propia
- Proxys: SOCKS5, HTTP/HTTPS
- WebRTC
- MQTT
- RDP/VNC (futuro)
- TLS/SSL
- Android/Termux
- Otros protocolos fácilmente integrables

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
- **Logger seguro y auditoría.**
- **Protección contra ataques de fuerza bruta y DoS.**
- **Integración opcional con HSM.**
- **Menú de configuración centralizado para todos los parámetros y preferencias.**
- **Sistema de notificaciones automáticas.**
- **Generación de reportes personalizados.**
- **Integración con APIs externas.**
- **Soporte para múltiples idiomas.**

## Modularidad y extensibilidad

- Cada protocolo y función es un plugin independiente.
- El core gestiona la carga dinámica de plugins, roles, permisos y configuración.
- Fácil de extender con nuevas funciones y protocolos.
