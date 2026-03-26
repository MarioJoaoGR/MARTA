
import json
import pytest
from your_module import is_json  # Replace 'your_module' with the actual module name where `is_json` is defined

@pytest.mark.parametrize("input_string, expected", [
    ('{"name": "Peter"}', True),
    ('[1, 2, 3]', True),
    ('{nope}', False),
    ('invalid json', False),
    ('   ', False),
    ('', False)
])
def test_valid_json_string(input_string, expected):
    assert is_json(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_json_0_test_valid_json_string
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:4:0: E0401: Unable to import 'your_module' (import-error)


"""