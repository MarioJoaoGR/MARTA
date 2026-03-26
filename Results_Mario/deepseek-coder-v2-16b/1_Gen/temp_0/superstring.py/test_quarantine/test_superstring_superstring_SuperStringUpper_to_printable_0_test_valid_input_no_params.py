
def test_to_printable():
    from superstring.superstring import SuperStringConcatenation, SuperStringBase
    
    left_string = SuperStringBase("Hello")
    right_string = SuperStringBase("World!")
    concatenated = SuperStringConcatenation(left_string, right_string)
    obj = SuperStringUpper(concatenated)
    
    assert obj.to_printable() == "HELLO WORLD!"
    assert obj.to_printable(start_index=6) == "WORLD!"
    assert obj.to_printable(end_index=5) == "HELLO"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_no_params
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_no_params.py:8:10: E0602: Undefined variable 'SuperStringUpper' (undefined-variable)


"""