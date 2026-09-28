from feature_flags import FeatureFlagCache, FeatureFlagRepository, FeatureFlagService
from feature_flags.repository import FeatureFlag
from feature_flags.service import LegacyFeatureFlagService


def create_service() -> FeatureFlagService:
    repository = FeatureFlagRepository()
    repository.save(FeatureFlag("tenant-alpha", "new-checkout", enabled=True))
    repository.save(FeatureFlag("tenant-beta", "new-checkout", enabled=False))
    return FeatureFlagService(repository, FeatureFlagCache())


def test_returns_same_value_for_repeated_lookup() -> None:
    service = create_service()

    assert service.is_enabled("tenant-alpha", "new-checkout") is True
    assert service.is_enabled("tenant-alpha", "new-checkout") is True


def test_returns_requested_tenant_value_after_prior_lookup() -> None:
    service = create_service()

    assert service.is_enabled("tenant-alpha", "new-checkout") is True
    assert service.is_enabled("tenant-beta", "new-checkout") is False


def test_cached_false_value_is_not_treated_as_a_miss() -> None:
    repository = FeatureFlagRepository()
    repository.save(FeatureFlag("tenant-alpha", "new-checkout", enabled=False))
    service = LegacyFeatureFlagService(repository, FeatureFlagCache())

    assert service.is_enabled("tenant-alpha", "new-checkout") is False
    repository.save(FeatureFlag("tenant-alpha", "new-checkout", enabled=True))

    assert service.is_enabled("tenant-alpha", "new-checkout") is False


def test_delete_normalizes_flag_name() -> None:
    repository = FeatureFlagRepository()
    repository.save(FeatureFlag("tenant-alpha", "New-Checkout", enabled=True))

    repository.delete("tenant-alpha", "NEW-CHECKOUT")

    assert repository.get("tenant-alpha", "new-checkout") is None


def test_list_for_tenant_does_not_leak_other_tenants() -> None:
    repository = FeatureFlagRepository()
    repository.save(FeatureFlag("tenant-alpha", "checkout", enabled=True))
    repository.save(FeatureFlag("tenant-beta", "billing", enabled=False))

    flags = repository.list_for_tenant("tenant-alpha")

    assert [(flag.tenant_id, flag.name) for flag in flags] == [
        ("tenant-alpha", "checkout")
    ]
