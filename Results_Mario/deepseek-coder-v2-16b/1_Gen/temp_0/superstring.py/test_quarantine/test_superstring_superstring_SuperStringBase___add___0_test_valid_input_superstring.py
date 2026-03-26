
from superstring.superstring import SuperStringBase, SuperString, SuperStringConcatenation

def test_valid_input_superstring():
    s1 = SuperStringBase()
    s2 = s1 + "Hello"
    assert str(s2) == "Hello", f"Expected 'Hello', but got {str(s2)}"
    
    s3 = SuperStringBase()
    s4 = s3 + SuperString("World")
    assert s4.concatenate() == "World", f"Expected 'World', but got {s4.concatenate()}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase___add___0_test_valid_input_superstring
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___0_test_valid_input_superstring.py:11:11: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___0_test_valid_input_superstring.py:11:69: E1101: Instance of 'SuperStringConcatenation' has no 'concatenate' member (no-member)


"""