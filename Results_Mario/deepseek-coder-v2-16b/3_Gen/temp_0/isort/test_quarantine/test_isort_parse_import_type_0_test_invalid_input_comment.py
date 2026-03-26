
from isort.parse import import_type
from isort.config import Config, DEFAULT_CONFIG
import pytest

@pytest.mark.parametrize("line, expected", [
    ("import os", "straight"),
    ("from math import sqrt", "from"),
    (" # This is a comment, no import here", None),
    ("# noqa: F401", "straight"),  # Since honor_noqa is False, the line with "noqa" is not ignored.
])
def test_import_type(line, expected):
    config = Config()
    config.honor_noqa = False
    assert import_type(line, config) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse_import_type_0_test_invalid_input_comment
isort/Test4DT_tests/test_isort_parse_import_type_0_test_invalid_input_comment.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_parse_import_type_0_test_invalid_input_comment.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""