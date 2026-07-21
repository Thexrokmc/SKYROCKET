import os


class SecretsManager:
    """
    Centralized access to application secrets.
    """

    def __init__(self):

        self._cache = {}

    def get(self, key: str, default=None):

        if key not in self._cache:
            self._cache[key] = os.getenv(key, default)

        return self._cache[key]

    def require(self, key: str):

        value = self.get(key)

        if value in (None, ""):
            raise ValueError(
                f"Missing required secret: {key}"
            )

        return value

    def has(self, key: str):

        return self.get(key) not in (None, "")

    def clear_cache(self):

        self._cache.clear()
