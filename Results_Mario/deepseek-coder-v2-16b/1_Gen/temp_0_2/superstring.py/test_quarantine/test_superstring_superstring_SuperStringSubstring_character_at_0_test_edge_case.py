
import pytest
from superstring import SuperStringBase
from superstring.superstring import SuperStringSubstring

@pytest.fixture
def setup_substring():
    base = SuperStringBase("Hello, World!")
    return SuperStringSubstring(base, 7, 12)

def test_character_at_edge_case(setup_substring):
    substring = setup_substring
    assert substring.character_at(0) == 'W'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring_character_at_0_test_edge_case
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_character_at_0_test_edge_case.py:3:0: E0611: No name 'SuperStringBase' in module 'superstring' (no-name-in-module)


"""