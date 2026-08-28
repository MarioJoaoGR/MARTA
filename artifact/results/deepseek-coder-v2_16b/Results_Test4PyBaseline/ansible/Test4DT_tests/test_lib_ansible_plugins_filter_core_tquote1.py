
# Module: ansible.plugins.filter.core
# test_core.py
from ansible.plugins.filter import core
import pytest

@pytest.mark.parametrize("input_string, expected", [
    ("hello world", "'hello world'"),
    (None, "''"),
    # Additional test cases to cover uncovered lines 103-105
    ("with space", "'with space'"),
    ("special!chars", "'special!chars'"),
    ("cmd.exe special chars ^&()%!@<>", "'cmd.exe special chars ^&()%!@<>'")
])
def test_quote(input_string, expected):
    assert core.quote(input_string) == expected
