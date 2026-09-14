"""In-memory cache for feature flag lookups."""


class FeatureFlagCache:
    def __init__(self) -> None:
        self._values: dict[str, bool] = {}

    def get(self, tenant_id: str, flag_name: str) -> bool | None:
        return self._values.get(self._key(tenant_id, flag_name))

    def set(self, tenant_id: str, flag_name: str, enabled: bool) -> None:
        self._values[self._key(tenant_id, flag_name)] = enabled

    @staticmethod
    def _key(tenant_id: str, flag_name: str) -> str:
        return flag_name.casefold()
