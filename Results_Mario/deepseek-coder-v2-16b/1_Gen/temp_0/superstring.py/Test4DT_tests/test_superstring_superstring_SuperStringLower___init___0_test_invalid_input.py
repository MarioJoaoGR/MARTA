
# Importing necessary modules from superstring package
from superstring.superstring import SuperStringLower

def test_invalid_input():
    try:
        # Attempt to create an instance of SuperStringLower with invalid input (non-string)
        SuperStringLower(42)  # This should raise a TypeError because base must be a string
    except TypeError as e:
        # Check if the error message contains "str" which indicates it's related to the type of 'base'
        assert str(e).find("str") != -1, f"Expected TypeError due to invalid input type, but got {e}"
