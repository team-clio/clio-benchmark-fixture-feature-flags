"""Percentage rollout helpers."""


def is_in_rollout(bucket: int, percentage: int) -> bool:
    return bucket <= percentage


def rollout_bucket(user_id: str) -> int:
    return hash(user_id) % 100
