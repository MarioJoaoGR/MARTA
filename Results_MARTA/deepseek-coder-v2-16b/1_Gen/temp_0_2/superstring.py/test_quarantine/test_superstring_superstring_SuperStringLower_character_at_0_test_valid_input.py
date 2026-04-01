
def test_valid_input():
    base = "Hello World"
    obj = SuperStringLower(base)
    assert obj._base == "hello world", f"Expected 'hello world', but got {obj._base}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringLower_character_at_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_valid_input.py:4:10: E0602: Undefined variable 'SuperStringLower' (undefined-variable)


"""