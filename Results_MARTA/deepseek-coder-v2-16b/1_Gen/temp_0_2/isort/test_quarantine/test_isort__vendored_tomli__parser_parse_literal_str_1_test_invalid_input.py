
from typing import Tuple

def parse_literal_str(src: str, pos: int) -> Tuple[int, str]:
    """Parses a literal string from the source code `src` starting at position `pos`.

    This function expects the string to be enclosed in single quotes (') and extracts the content between these quotes. It skips over the initial apostrophe and finds the ending apostrophe to return the substring representing the literal string.

    Parameters:
        src (str): The input string containing the source code, which is expected to contain a literal string enclosed in single quotes.
        pos (int): The current position within `src` from where the parsing should start. This is an integer index indicating the character offset within the string.

    Returns:
        Tuple[int, str]: A tuple containing the new position after skipping the ending apostrophe and the substring of `src` that lies between the initial and ending apostrophes.

    Raises:
        ValueError: If the literal string is not properly closed by an apostrophe.
    """
    pos += 1  # Skip starting apostrophe
    start_pos = pos
    try:
        pos = skip_until(src, pos, "'", error_on=ILLEGAL_LITERAL_STR_CHARS, error_on_eof=True)
    except ValueError as e:
        raise ValueError("SyntaxError: Unterminated string literal.") from e
    
    return pos + 1, src[start_pos:pos]  # Skip ending apostrophe

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_literal_str_1_test_invalid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_1_test_invalid_input.py:22:14: E0602: Undefined variable 'skip_until' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_1_test_invalid_input.py:22:49: E0602: Undefined variable 'ILLEGAL_LITERAL_STR_CHARS' (undefined-variable)


"""