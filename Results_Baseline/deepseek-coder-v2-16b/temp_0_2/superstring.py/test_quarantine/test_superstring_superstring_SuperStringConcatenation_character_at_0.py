
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringConcatenation

# Test cases for concatenate method with default separator (space)
def test_concatenate_default():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.concatenate() == "Hello World"

# Test cases for concatenate method with custom separator
def test_concatenate_custom_separator():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.concatenate("_") == "Hello_World"

# Test cases for character_at method
def test_character_at_valid_index():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.character_at(0) == 'H'  # First character of left string
    assert ssc.character_at(5) == 'W'  # First character of right string

def test_character_at_invalid_index():
    ssc = SuperStringConcatenation("Hello", "World")
    with pytest.raises(IndexError):
        ssc.character_at(10)  # Index out of range for both strings

# Test cases for length method (not explicitly defined in the class, but implied by character_at and concatenate tests)
def test_length():
    ssc = SuperStringConcatenation("Hello", "World")
    assert len(ssc.concatenate()) == 10  # Length of concatenated string "Hello World"

# Test cases for to_printable method (not explicitly defined in the class, but implied by character_at)
def test_to_printable():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.to_printable(start_index=0) == "Hello"  # Substring starting from index 0
    assert ssc.to_printable(start_index=6) == "World"  # Substring starting from index 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_character_at_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0.py:9:11: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0.py:14:11: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0.py:30:15: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)


"""