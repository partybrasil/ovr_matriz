from abc import ABC, abstractmethod

class IPlugin(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def initialize(self, app_context):
        pass
