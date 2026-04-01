
import json
from typing import Any

def is_full_string(input_string: str) -> bool:
    return bool(input_string and not input_string.isspace())

def is_json(input_string: Any) -> bool:
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            return isinstance(json.loads(input_string), (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass
    return False

import pytest

@pytest.mark.parametrize("non_string_input", [None, 123, [], {}, set(), object()])
def test_non_string_input(non_string_input):
    assert not is_json(non_string_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_json_1_test_non_string_input
python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_1_test_non_string_input.py:9:40: E0602: Undefined variable 'JSON_WRAPPER_RE' (undefined-variable)


"""