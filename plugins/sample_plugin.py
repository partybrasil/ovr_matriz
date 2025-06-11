from .base_plugin import BasePlugin

class SamplePlugin(BasePlugin):
    name = "SamplePlugin"

    def initialize(self, app_context):
        """Initializes the plugin with the given application context.

        Args:
            app_context: The application context to initialize the plugin with.
        """
        self.app_context = app_context
        print(f"[{self.name}] initialized with context: {app_context}")

    def activate(self):
        """Activates the plugin, enabling its functionality."""
        super().activate()
        print(f"[{self.name}] activated")

    def deactivate(self):
        """Deactivates the plugin, disabling its functionality."""
        super().deactivate()
        print(f"[{self.name}] deactivated")

    def do_something(self):
        """Executes a sample action, demonstrating the plugin's functionality."""
        print(f"[{self.name}] Doing something useful!")
