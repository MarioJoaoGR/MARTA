
from isort._vendored.tomli._parser import parse_key, parse_value, skip_chars
from isort._vendored.tomli._shared_types import Pos, Key, Any, ParseFloat, suffixed_err
from typing import Tuple, Optional

def parse_key_value_pair(src: str, pos: Pos, parse_float: ParseFloat) -> Tuple[Pos, Key, Any]:
    """Parses a key/value pair from the input source `src` starting at position `pos`.

    This function is designed to extract key-value pairs in a TOML-like format from the given string. It begins by parsing the key using `parse_key(src, pos)`, then checks for an equals sign (`=`) to confirm it's part of a key-value pair. Afterward, it parses the value associated with the key using `parse_value(src, pos, parse_float).

    Parameters:
        src (str): The input string from which to parse the key/value pair. This should be the complete content of the file or data structure being parsed.
        pos (Pos): The starting position in `src` from where to begin parsing the key/value pair. This is typically an index indicating the character offset from the start of the string.
        parse_float (ParseFloat): A callable that converts a string representation of a number into its float equivalent. This allows for custom handling of numeric strings, such as those representing floating-point numbers.

    Returns:
        Tuple[Pos, Key, Any]: A tuple containing the updated position after parsing the key/value pair, the parsed key content as a tuple of its parts, and the parsed value.

    Raises:
        IndexError: If attempting to access a position beyond the end of the string `src`.
        ValueError: If an illegal character is encountered or if there's an attempt to parse multi-line strings without proper termination with triple quotes.
        suffixed_err: If an unterminated string is detected, it raises a custom error prefixed with the source content and position details.
    """
    pos, key = parse_key(src, pos)
    try:
        char: Optional[str] = src[pos]
    except IndexError:
        char = None
    if char != "=":
        raise suffixed_err(src, pos, 'Expected "=" after a key in a key/value pair')
    pos += 1
    pos = skip_chars(src, pos, TOML_WS)
    pos, value = parse_value(src, pos, parse_float)
    return pos, key, value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_none_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_none_input.py:3:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_none_input.py:3:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_none_input.py:32:31: E0602: Undefined variable 'TOML_WS' (undefined-variable)


"""