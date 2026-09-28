"""Storage abstraction for tenant feature flags."""

from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureFlag:
    tenant_id: str
    name: str
    enabled: bool


class FeatureFlagRepository:
    def __init__(self) -> None:
        self._flags: dict[tuple[str, str], FeatureFlag] = {}

    def save(self, flag: FeatureFlag) -> None:
        self._flags[(flag.tenant_id, flag.name.casefold())] = flag

    def get(self, tenant_id: str, flag_name: str) -> FeatureFlag | None:
        return self._flags.get((tenant_id, flag_name.casefold()))

    def delete(self, tenant_id: str, flag_name: str) -> None:
        self._flags.pop((tenant_id, flag_name), None)

    def list_for_tenant(self, tenant_id: str) -> list[FeatureFlag]:
        return list(self._flags.values())
