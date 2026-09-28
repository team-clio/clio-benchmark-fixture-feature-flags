import os
import subprocess
import sys

from feature_flags.rollout import is_in_rollout


def test_percentage_boundary_excludes_bucket_equal_to_percentage() -> None:
    assert is_in_rollout(bucket=10, percentage=10) is False


def test_rollout_bucket_is_stable_across_processes() -> None:
    command = [
        sys.executable,
        "-c",
        "from feature_flags.rollout import rollout_bucket;"
        "print(rollout_bucket('user-42'))",
    ]
    first = subprocess.check_output(
        command,
        text=True,
        env={**os.environ, "PYTHONHASHSEED": "1"},
    ).strip()
    second = subprocess.check_output(
        command,
        text=True,
        env={**os.environ, "PYTHONHASHSEED": "2"},
    ).strip()

    assert first == second
