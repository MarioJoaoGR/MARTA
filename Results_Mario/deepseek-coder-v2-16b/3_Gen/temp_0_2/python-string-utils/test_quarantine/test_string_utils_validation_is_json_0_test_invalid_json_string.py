
import json
from typing import Any

def is_full_string(input_string: str) -> bool:
    return bool(input_string and input_string.strip())

def is_json(input_string: Any) -> bool:
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            return isinstance(json.loads(input_string), (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass
    return False

import pytest

@pytest.mark.parametrize("invalid_json", [
    "{nope}",
    "None",  # This is a string representation of None, not JSON
    "",
    " ",
    "invalid json",
    "12345",  # This is an integer, not JSON
])
def test_invalid_json_string(invalid_json):
    assert not is_json(invalid_json)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_json_0_test_invalid_json_string
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_invalid_json_string.py:9:40: E0602: Undefined variable 'JSON_WRAPPER_RE' (undefined-variable)


"""