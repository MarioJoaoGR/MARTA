
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, BASIC_STR_ESCAPE_REPLACEMENTS
from isort._shared_lib import Pos, skip_chars, suffixed_err

# Assuming TOML_WS and related constants are defined in _parser or similar module
TOML_WS = " \t"  # Example definition for context; adjust as necessary
TOML_WS_AND_NEWLINE = " \t\n"  # Example definition for context; adjust as necessary

def test_invalid_escape_sequence():
    src = "Hello\\xWorld"
    pos = 0
    with pytest.raises(ValueError) as excinfo:
        new_pos, parsed_str = parse_basic_str_escape(src, pos)
    assert str(excinfo.value) == 'Unescaped "\\" in a string'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_invalid_escape_sequence
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_invalid_escape_sequence.py:4:0: E0401: Unable to import 'isort._shared_lib' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_invalid_escape_sequence.py:4:0: E0611: No name '_shared_lib' in module 'isort' (no-name-in-module)


"""