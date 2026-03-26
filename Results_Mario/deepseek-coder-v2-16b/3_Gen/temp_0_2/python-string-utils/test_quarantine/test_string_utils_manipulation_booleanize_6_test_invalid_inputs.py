
def booleanize(input_string: str) -> bool:
    """
    Turns a string into a boolean based on its content (CASE INSENSITIVE).

    A positive boolean (True) is returned if the string value is one of the following:

    - "true"
    - "1"
    - "yes"
    - "y"

    Otherwise False is returned.

    *Examples:*

    >>> booleanize('true') # returns True
    >>> booleanize('YES') # returns True
    >>> booleanize('nope') # returns False

    :param input_string: String to convert
    :type input_string: str
    :return: True if the string contains a boolean-like positive value, false otherwise
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    normalized_input = input_string.lower()
    return normalized_input in ('true', '1', 'yes', 'y')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_6_test_invalid_inputs
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_6_test_invalid_inputs.py:25:11: E0602: Undefined variable 'is_string' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_6_test_invalid_inputs.py:26:14: E0602: Undefined variable 'InvalidInputError' (undefined-variable)


"""