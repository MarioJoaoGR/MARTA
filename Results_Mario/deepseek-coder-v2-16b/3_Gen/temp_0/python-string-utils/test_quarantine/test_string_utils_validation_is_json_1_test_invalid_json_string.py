
import json
from typing import Any

def is_full_string(input_string: str) -> bool:
    return bool(input_string and not input_string.isspace())

JSON_WRAPPER_RE = None  # Assuming this is defined elsewhere in the codebase

def is_json(input_string: Any) -> bool:
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            return isinstance(json.loads(input_string), (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass
    return False

import pytest

@pytest.mark.parametrize("invalid_json", [
    '{nope}',
    '',
    ' ',
    None,
])
def test_invalid_json_string(invalid_json):
    assert not is_json(invalid_json)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_1_test_invalid_json_string.py F [ 25%]
...                                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_json_string[{nope}] _______________________

invalid_json = '{nope}'

    @pytest.mark.parametrize("invalid_json", [
        '{nope}',
        '',
        ' ',
        None,
    ])
    def test_invalid_json_string(invalid_json):
>       assert not is_json(invalid_json)

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_1_test_invalid_json_string.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = '{nope}'

    def is_json(input_string: Any) -> bool:
>       if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
E       AttributeError: 'NoneType' object has no attribute 'match'

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_1_test_invalid_json_string.py:11: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_1_test_invalid_json_string.py::test_invalid_json_string[{nope}]
========================= 1 failed, 3 passed in 0.03s ==========================
"""