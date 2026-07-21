from abc import ABC
from typing import Dict, List


class Plugin(ABC):
    """
    Base class for all SKYROCKET plugins.
    """

    name = "Unnamed Plugin"
    version = "1.0.0"

    def initialize(self):
        pass

    def shutdown(self):
        pass


class PluginManager:

    def __init__(self):

        self._plugins: Dict[str, Plugin] = {}

    def register(self, plugin: Plugin):

        if plugin.name in self._plugins:
            raise ValueError(
                f"Plugin '{plugin.name}' already registered."
            )

        plugin.initialize()

        self._plugins[plugin.name] = plugin

    def unregister(self, name: str):

        plugin = self._plugins.pop(name)

        plugin.shutdown()

    def get(self, name: str):

        return self._plugins[name]

    def exists(self, name: str):

        return name in self._plugins

    def list_plugins(self) -> List[str]:

        return sorted(self._plugins.keys())

    def shutdown_all(self):

        for plugin in list(self._plugins.values()):

            plugin.shutdown()

        self._plugins.clear()
