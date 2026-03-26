
import sys
from unittest.mock import patch

import pytest


def ask_whether_to_apply_changes_to_file(file_path: str) -> bool:
    answer = None
    while answer not in ("yes", "y", "no", "n", "quit", "q"):
        answer = input(f"Apply suggested changes to '{file_path}' [y/n/q]? ")  # nosec
        answer = answer.lower()
        if answer in ("no", "n"):
            return False
        if answer in ("quit", "q"):
            sys.exit(1)
    return True

@pytest.mark.parametrize("mock_input, expected", [("n", False), ("N", False)])
def test_valid_input_no(mock_input, expected):
    with patch('builtins.input', lambda _: mock_input):
        assert ask_whether_to_apply_changes_to_file("example.txt") == expected
