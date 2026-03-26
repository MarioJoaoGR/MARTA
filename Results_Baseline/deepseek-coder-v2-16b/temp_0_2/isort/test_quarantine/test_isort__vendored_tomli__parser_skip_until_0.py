
# Module: Test4DT_tests.test_isort__vendored_tomli__parser_skip_until_0
import pytest
from typing import FrozenSet
from isort._parser import skip_until, Pos  # Corrected import statement

def test_skip_until_typical():
    src = "let x = 10\nprint(x)"
    pos = 7
    expect = "\n"
    new_pos = skip_until(src, pos, expect, error_on={"="}, error_on_eof=False)
    assert new_pos == 8, f"Expected position of newline character to be 8 but got {new_pos}"

def test_skip_until_error_on_eof():
    src = "let x = 10\nprint(x)"
    pos = 7
    expect = "\n"
    with pytest.raises(Exception) as e:
        skip_until(src, pos, expect, error_on={"="}, error_on_eof=True)
    assert str(e.value) == "Expected \"\\n\"", f"Error message should indicate expected substring not found but got {str(e.value)}"

def test_skip_until_error_on_invalid_character():
    src = "let x = 10\nprint(x)"
    pos = 7
    expect = "\n"
    with pytest.raises(Exception) as e:
        skip_until(src, pos, expect, error_on={"="}, error_on_eof=False)
    assert str(e.value).endswith("Found invalid character \"\\n\""), f"Error message should indicate found invalid character but got {str(e.value)}"

def test_skip_until_no_error():
    src = "let x = 10\nprint(x)"
    pos = 7
    expect = "\n"
    new_pos = skip_until(src, pos, expect, error_on={"="}, error_on_eof=False)
    assert new_pos == 8, f"Expected position of newline character to be 8 but got {new_pos}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_skip_until_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0.py:5:0: E0401: Unable to import 'isort._parser' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_0.py:5:0: E0611: No name '_parser' in module 'isort' (no-name-in-module)


"""