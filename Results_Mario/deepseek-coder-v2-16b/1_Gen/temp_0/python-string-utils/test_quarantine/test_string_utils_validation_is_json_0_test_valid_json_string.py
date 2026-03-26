
import json
from typing import Any

def is_full_string(input_string: str) -> bool:
    return bool(input_string and not input_string.isspace())

JSON_WRAPPER_RE = None  # Assuming this is defined somewhere in the module, but for testing purposes, we don't need it to be set.

def is_json(input_string: Any) -> bool:
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            return isinstance(json.loads(input_string), (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass
    return False

import pytest

@pytest.mark.parametrize("test_input, expected", [
    ('{"name": "Peter"}', True),
    ('[1, 2, 3]', True),
    ('{nope}', False),
    ('', False),
    (' ', False),
    (None, False)
])
def test_valid_json_string(test_input, expected):
    assert is_json(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py F [ 16%]
FF...                                                                    [100%]

=================================== FAILURES ===================================
________________ test_valid_json_string[{"name": "Peter"}-True] ________________

test_input = '{"name": "Peter"}', expected = True

    @pytest.mark.parametrize("test_input, expected", [
        ('{"name": "Peter"}', True),
        ('[1, 2, 3]', True),
        ('{nope}', False),
        ('', False),
        (' ', False),
        (None, False)
    ])
    def test_valid_json_string(test_input, expected):
>       assert is_json(test_input) == expected

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = '{"name": "Peter"}'

    def is_json(input_string: Any) -> bool:
>       if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
E       AttributeError: 'NoneType' object has no attribute 'match'

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:11: AttributeError
____________________ test_valid_json_string[[1, 2, 3]-True] ____________________

test_input = '[1, 2, 3]', expected = True

    @pytest.mark.parametrize("test_input, expected", [
        ('{"name": "Peter"}', True),
        ('[1, 2, 3]', True),
        ('{nope}', False),
        ('', False),
        (' ', False),
        (None, False)
    ])
    def test_valid_json_string(test_input, expected):
>       assert is_json(test_input) == expected

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = '[1, 2, 3]'

    def is_json(input_string: Any) -> bool:
>       if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
E       AttributeError: 'NoneType' object has no attribute 'match'

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:11: AttributeError
_____________________ test_valid_json_string[{nope}-False] _____________________

test_input = '{nope}', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('{"name": "Peter"}', True),
        ('[1, 2, 3]', True),
        ('{nope}', False),
        ('', False),
        (' ', False),
        (None, False)
    ])
    def test_valid_json_string(test_input, expected):
>       assert is_json(test_input) == expected

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = '{nope}'

    def is_json(input_string: Any) -> bool:
>       if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
E       AttributeError: 'NoneType' object has no attribute 'match'

python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py:11: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py::test_valid_json_string[{"name": "Peter"}-True]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py::test_valid_json_string[[1, 2, 3]-True]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_json_0_test_valid_json_string.py::test_valid_json_string[{nope}-False]
========================= 3 failed, 3 passed in 0.02s ==========================

"""