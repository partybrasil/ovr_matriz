from .base_plugin import BasePlugin
from core.logger import logger
from core.roles import has_permission

class MeshPlugin(BasePlugin):
    name = "Mesh"

    def initialize(self, app_context):
        self.app_context = app_context

    def join_mesh(self, mesh_id):
        logger.info(f"[Mesh] Placeholder: unir a mesh {mesh_id}.")
