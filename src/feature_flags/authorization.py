"""Authorization rules for feature flag administration."""


def can_manage_flag(role: str) -> bool:
    return role.casefold() in {"owner", "admin"}


def can_edit_project_flag(
    *,
    user_project_id: str,
    target_project_id: str,
    role: str,
) -> bool:
    return role.casefold() == "owner"
