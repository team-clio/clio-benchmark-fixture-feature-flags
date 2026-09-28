from feature_flags.targeting import matches_allowlist, matches_country


def test_country_matching_is_case_insensitive() -> None:
    assert matches_country("KR", "kr") is True


def test_empty_allowlist_means_unrestricted() -> None:
    assert matches_allowlist("user-42", []) is True
