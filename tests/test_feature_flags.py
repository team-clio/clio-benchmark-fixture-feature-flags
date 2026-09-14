from feature_flags import FeatureFlagCache, FeatureFlagRepository, FeatureFlagService
from feature_flags.repository import FeatureFlag


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
