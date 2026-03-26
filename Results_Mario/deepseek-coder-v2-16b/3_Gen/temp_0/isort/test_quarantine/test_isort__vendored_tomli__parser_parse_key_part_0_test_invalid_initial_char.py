
from typing import Tuple
from isort._vendored.tomli._parser import parse_key_part, Pos, BARE_KEY_CHARS, suffixed_err

def test_invalid_initial_char():
    src = "!abc"  # Invalid initial character for a key part
    pos = Pos(0)
    
    try:
        new_pos, parsed_key = parse_key_part(src, pos)
    except suffixed_err as e:
        assert str(e) == f"{src}:{pos.i} Invalid initial character for a key part"
        return  # Test passed
    
    assert False, "Expected suffixed_err was not raised"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_key_part_0_test_invalid_initial_char
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_invalid_initial_char.py:11:11: E0712: Catching an exception which doesn't inherit from Exception: suffixed_err (catching-non-exception)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_invalid_initial_char.py:12:34: E1101: Instance of 'int' has no 'i' member (no-member)


"""