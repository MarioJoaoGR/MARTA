
import json
from typing import Any

def is_full_string(input_string: str) -> bool:
    return input_string and input_string.strip()

def is_json(input_string: Any) -> bool:
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            return isinstance(json.loads(input_string), (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass
    return False

import pytest

@pytest.mark.parametrize("input_string", [None])
def test_none_input(input_string):
    assert not is_json(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_json_1_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_1_test_none_input.py:9:40: E0602: Undefined variable 'JSON_WRAPPER_RE' (undefined-variable)


"""