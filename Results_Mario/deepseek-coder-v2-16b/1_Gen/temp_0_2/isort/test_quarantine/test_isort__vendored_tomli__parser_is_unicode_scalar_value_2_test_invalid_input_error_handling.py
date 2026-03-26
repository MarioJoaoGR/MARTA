
def is_unicode_scalar_value(codepoint: int) -> bool:
    """
    Determines whether the given integer represents a Unicode scalar value.

    A Unicode scalar value is any code point in the range from U+0000 to U+D7FF, inclusive, or in the range from U+E000 to U+110000, inclusive. This function checks if a given integer falls within either of these ranges and returns True if it does, otherwise False.

    Parameters:
        codepoint (int): An integer representing a Unicode code point.

        Usage:
            To check if a specific Unicode code point is valid and within the allowed scalar ranges, use this function by passing an integer representing the codepoint. The result will indicate whether the codepoint falls within the specified Unicode scalar value range.

    Returns:
        bool: True if the codepoint is a valid Unicode scalar value, False otherwise.

    Examples:
        >>> is_unicode_scalar_value(65)  # ASCII 'A'
        True
        >>> is_unicode_scalar_value(1048575)  # U+FFFFF
        True
        >>> is_unicode_scalar_value(-5)  # Negative value
        False
        >>> is_unicode_scalar_value(1114112)  # Out of range (U+10FFFF + 1)
        False
    """
    return (0 <= codepoint <= 55295) or (57344 <= codepoint <= 1114111)

def test_invalid_input_error_handling():
    # Test cases with invalid inputs
    assert not is_unicode_scalar_value(0)  # U+0000

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_is_unicode_scalar_value_2_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        # Test cases with invalid inputs
>       assert not is_unicode_scalar_value(0)  # U+0000
E       assert not True
E        +  where True = is_unicode_scalar_value(0)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_is_unicode_scalar_value_2_test_invalid_input_error_handling.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_is_unicode_scalar_value_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.08s ===============================
"""