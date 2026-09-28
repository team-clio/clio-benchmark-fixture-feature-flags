from feature_flags.authorization import can_edit_project_flag, can_manage_flag


def test_admin_cannot_manage_owner_only_flag() -> None:
    assert can_manage_flag("admin") is False


def test_owner_cannot_edit_another_project() -> None:
    assert (
        can_edit_project_flag(
            user_project_id="project-alpha",
            target_project_id="project-beta",
            role="owner",
        )
        is False
    )
