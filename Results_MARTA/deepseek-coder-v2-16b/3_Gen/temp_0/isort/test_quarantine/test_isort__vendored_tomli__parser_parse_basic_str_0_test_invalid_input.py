
import pytest
from isort._vendored.tomli._parser import parse_basic_str
from isort._vendored.tomli._shared_types import Pos
from isort._vendored.tomli._errors import suffixed_err

def test_parse_basic_str_invalid_input():
    with pytest.raises(suffixed_err) as excinfo:
        parse_basic_str("invalid input", Pos(0), multiline=False)
    assert "Unterminated string" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input.py:4:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input.py:4:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input.py:5:0: E0401: Unable to import 'isort._vendored.tomli._errors' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input.py:5:0: E0611: No name '_errors' in module 'isort._vendored.tomli' (no-name-in-module)


"""