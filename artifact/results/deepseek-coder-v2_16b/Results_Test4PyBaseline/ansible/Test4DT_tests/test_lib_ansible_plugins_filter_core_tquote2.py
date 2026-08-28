
# Module: ansible.plugins.filter.core
# test_core.py
from ansible.plugins.filter import core
import pytest

@pytest.mark.parametrize("input_string, expected", [
    ("hello world", "'hello world'"),
    (None, "''")
])
def test_quote(input_string, expected):
    assert core.quote(input_string) == expected

# Additional tests for uncovered lines 103-105

def test_quote_none():
    # Test when input is None
    result = core.quote(None)