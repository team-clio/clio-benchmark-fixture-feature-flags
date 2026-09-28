"""Audience targeting rules."""


def matches_country(rule_country: str, request_country: str) -> bool:
    return rule_country == request_country


def matches_allowlist(user_id: str, allowed_user_ids: list[str]) -> bool:
    return user_id in allowed_user_ids
