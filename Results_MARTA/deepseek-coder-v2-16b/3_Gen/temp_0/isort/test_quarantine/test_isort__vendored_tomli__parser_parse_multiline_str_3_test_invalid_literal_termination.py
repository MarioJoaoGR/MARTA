
from isort._vendored.tomli._parser import parse_multiline_str
from isort._vendored.tomli._constants import ILLEGAL_MULTILINE_LITERAL_STR_CHARS
from isort._vendored.tomli.pos import Pos
import pytest

def test_invalid_literal_termination():
    with pytest.raises(ValueError, match="Illegal character"):
        parse_multiline_str("'''\nabc", Pos(0), literal=True)

    with pytest.raises(ValueError, match="Illegal character"):
        parse_multiline_str("'''abc\ndef", Pos(0), literal=True)

    # Test for basic multi-line string which should not raise an error
    pos, result = parse_multiline_str('"""\nabc', Pos(0), literal=False)
    assert result == "\nabc"
    assert pos == 3 + len("\nabc")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_multiline_str_3_test_invalid_literal_termination
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_invalid_literal_termination.py:3:0: E0401: Unable to import 'isort._vendored.tomli._constants' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_invalid_literal_termination.py:3:0: E0611: No name '_constants' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_invalid_literal_termination.py:4:0: E0401: Unable to import 'isort._vendored.tomli.pos' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_invalid_literal_termination.py:4:0: E0611: No name 'pos' in module 'isort._vendored.tomli' (no-name-in-module)


"""