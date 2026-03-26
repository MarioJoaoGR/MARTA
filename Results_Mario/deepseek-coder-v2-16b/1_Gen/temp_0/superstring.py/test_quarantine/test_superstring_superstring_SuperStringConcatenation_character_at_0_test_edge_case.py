
import pytest
from superstring.superstring import SuperStringConcatenation, ConcreteSuperString

@pytest.fixture
def setup_concatenation():
    left_string = ConcreteSuperString("Hello")
    right_string = ConcreteSuperString("World!")
    return SuperStringConcatenation(left_string, right_string)

def test_character_at_within_left_string(setup_concatenation):
    concatenated = setup_concatenation
    assert concatenated.character_at(0) == 'H'
    assert concatenated.character_at(4) == 'o'

def test_character_at_within_right_string(setup_concatenation):
    concatenated = setup_concatenation
    assert concatenated.character_at(5) == 'W'
    assert concatenated.character_at(9) == '!'

def test_character_at_out_of_bounds(setup_concatenation):
    concatenated = setup_concatenation
    with pytest.raises(IndexError):
        concatenated.character_at(12)  # Length is 12, so index 12 is out of bounds

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py:3:0: E0611: No name 'ConcreteSuperString' in module 'superstring.superstring' (no-name-in-module)


"""