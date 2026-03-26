
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringConcatenation, ConcreteSuperString

def test_character_at():
    # Create mocks for the left and right strings
    left_mock = MagicMock()
    right_mock = MagicMock()
    
    # Set up the length method for both mocks
    left_mock.length.return_value = 5
    right_mock.length.return_value = 8
    
    # Set up the character at index methods for both mocks
    left_mock.__getitem__.side_effect = lambda idx: "Hello"[idx] if idx < len("Hello") else ""
    right_mock.__getitem__.side_effect = lambda idx: "World!"[idx - len("Hello")] if idx >= len("Hello") else ""
    
    # Create an instance of SuperStringConcatenation with the mocks
    concatenated = SuperStringConcatenation(left_mock, right_mock)
    
    # Test character at valid index within left string
    assert concatenated.character_at(2) == 'l'
    
    # Test character at valid index within right string
    assert concatenated.character_at(7) == 'W'
    
    # Test character at invalid index (should raise an error or return None/empty based on implementation)
    with pytest.raises(IndexError):  # Adjust the exception type if necessary
        concatenated.character_at(15)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_character_at_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_valid_input.py:4:0: E0611: No name 'ConcreteSuperString' in module 'superstring.superstring' (no-name-in-module)


"""