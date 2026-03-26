
from superstring.superstring import SuperString
from unittest.mock import MagicMock
import pytest

def test_valid_input():
    # Create a mock SuperString instance
    base_mock = MagicMock()
    base_mock.character_at = MagicMock(return_value="H")
    
    # Instantiate the SuperStringLower with the mocked SuperString
    superstring_lower = SuperStringLower(base_mock)
    
    # Call the character_at method and check if it returns the expected lowercase 'h'
    assert superstring_lower.character_at(0) == "h"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringLower_character_at_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_valid_input.py:12:24: E0602: Undefined variable 'SuperStringLower' (undefined-variable)


"""