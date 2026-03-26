
from superstring.superstring import SuperStringConcatenation, SuperStringSubstring

def test_valid_input():
    left_substr = SuperStringSubstring("Hello", 0, 5)
    right_substr = SuperStringSubstring("World!", 0, 5)
    setup = SuperStringConcatenation(left_substr, right_substr)
    assert setup.concatenate() == 'HelloWorld!'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_character_at_1_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_1_test_valid_input.py:8:11: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)


"""