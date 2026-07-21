from typing import Any


class ServiceContainer:
    """
    Simple dependency injection container.
    """

    def __init__(self):
        self._services = {}

    def register(self, name: str, service: Any):

        if name in self._services:
            raise ValueError(
                f"Service '{name}' already registered."
            )

        self._services[name] = service

    def resolve(self, name: str):

        if name not in self._services:
            raise KeyError(
                f"Service '{name}' is not registered."
            )

        return self._services[name]

    def has(self, name: str):

        return name in self._services

    def remove(self, name: str):

        self._services.pop(name, None)

    def clear(self):

        self._services.clear()

    def list_services(self):

        return sorted(self._services.keys())
