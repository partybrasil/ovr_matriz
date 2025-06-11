from abc import ABC, abstractmethod

class BasePlugin(ABC):
    name: str
    active: bool = False

    @abstractmethod
    def initialize(self, app_context):
        pass

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def configure(self, **kwargs):
        """Configura el plugin con parámetros arbitrarios."""
        for k, v in kwargs.items():
            setattr(self, k, v)
