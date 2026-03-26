
import sys
from unittest.mock import patch
import pytest
from isort.format import ask_whether_to_apply_changes_to_file

@pytest.mark.parametrize("input_value, expected", [
    ("y", True),
    ("n", False),
    ("q", None)
])
def test_invalid_input_quit(capsys, input_value, expected):
    with patch('builtins.input', return_value=input_value):
        if expected is None:
            with pytest.raises(SystemExit) as excinfo:
                ask_whether_to_apply_changes_to_file("example.txt")
            assert excinfo.value.code == 1
        else:
            assert ask_whether_to_apply_changes_to_file("example.txt") == expected
