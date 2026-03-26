
import pytest
from superstring import SuperStringSubstring

# Fixture to create an instance of SuperStringSubstring for testing
@pytest.fixture
def setup_substring():
    return SuperStringSubstring("Hello, World!", 7, 12)

def test_character_at_0(setup_substring):
    assert setup_substring.character_at(0) == 'W'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring_character_at_0_test_edge_cases
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_character_at_0_test_edge_cases.py:3:0: E0611: No name 'SuperStringSubstring' in module 'superstring' (no-name-in-module)


"""