
from unittest.mock import patch
from uuid import uuid4
from string_utils.manipulation import __placeholder_key

def test_none_input():
    try:
        formatter = __StringFormatter(None)
    except InvalidInputError as e:
        assert str(e) == "Expected 'str', received 'NoneType'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:4:0: E0611: No name '__placeholder_key' in module 'string_utils.manipulation' (no-name-in-module)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:8:20: E0602: Undefined variable '__StringFormatter' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_none_input.py:9:11: E0602: Undefined variable 'InvalidInputError' (undefined-variable)

"""