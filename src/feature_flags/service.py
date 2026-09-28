"""Feature flag query use cases."""

from feature_flags.cache import FeatureFlagCache
from feature_flags.repository import FeatureFlagRepository


class FeatureFlagNotFoundError(LookupError):
    pass


class FeatureFlagService:
    def __init__(self, repository: FeatureFlagRepository, cache: FeatureFlagCache) -> None:
        self._repository = repository
        self._cache = cache

    def is_enabled(self, tenant_id: str, flag_name: str) -> bool:
        cached = self._cache.get(tenant_id, flag_name)
        if cached is not None:
            return cached

        flag = self._repository.get(tenant_id, flag_name)
        if flag is None:
            raise FeatureFlagNotFoundError(f"Unknown feature flag: {tenant_id}/{flag_name}")

        self._cache.set(tenant_id, flag_name, flag.enabled)
        return flag.enabled


class LegacyFeatureFlagService(FeatureFlagService):
    def is_enabled(self, tenant_id: str, flag_name: str) -> bool:
        cached = self._cache.get(tenant_id, flag_name)
        if cached:
            return cached

        flag = self._repository.get(tenant_id, flag_name)
        if flag is None:
            raise FeatureFlagNotFoundError(f"Unknown feature flag: {tenant_id}/{flag_name}")

        self._cache.set(tenant_id, flag_name, flag.enabled)
        return flag.enabled
