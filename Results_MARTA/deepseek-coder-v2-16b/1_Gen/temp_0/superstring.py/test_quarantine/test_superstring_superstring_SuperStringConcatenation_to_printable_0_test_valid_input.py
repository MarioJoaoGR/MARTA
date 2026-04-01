
import pytest
from superstring.superstring import SuperStringConcatenation, ConcreteSuperString

@pytest.fixture
def setup_concatenation():
    left_string = ConcreteSuperString("Hello")
    right_string = ConcreteSuperString("World!")
    return SuperStringConcatenation(left_string, right_string)

def test_to_printable_default(setup_concatenation):
    concatenated = setup_concatenation
    assert concatenated.to_printable() == "HelloWorld!"

def test_to_printable_with_start_index(setup_concatenation):
    concatenated = setup_concatenation
    assert concatenated.to_printable(start_index=6) == "World!"

def test_to_printable_with_end_index(setup_concatenation):
    concatenated = setup_concatenation
    assert concatenated.to_printable(end_index=5) == "Hello"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_valid_input.py:3:0: E0611: No name 'ConcreteSuperString' in module 'superstring.superstring' (no-name-in-module)


"""