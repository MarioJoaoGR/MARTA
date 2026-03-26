
import pytest
from collections import defaultdict
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe
from typing import Mapping

@pytest.mark.parametrize("test_input, expected", [
    (defaultdict(int), True),
    (dict, True),
    ([], False),
    ({}, True),  # Adding a test case for dict-like object
    ((), False),   # Adding a test case for tuple which is not a mapping
])
def test_valid_case_defaultdict(test_input, expected):
    assert _is_mapping(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_defaultdict.py F [ 20%]
..F.                                                                     [100%]

=================================== FAILURES ===================================
________________ test_valid_case_defaultdict[test_input0-True] _________________

test_input = defaultdict(<class 'int'>, {}), expected = True

    @pytest.mark.parametrize("test_input, expected", [
        (defaultdict(int), True),
        (dict, True),
        ([], False),
        ({}, True),  # Adding a test case for dict-like object
        ((), False),   # Adding a test case for tuple which is not a mapping
    ])
    def test_valid_case_defaultdict(test_input, expected):
>       assert _is_mapping(test_input) == expected
E       AssertionError: assert False == True
E        +  where False = _is_mapping(defaultdict(<class 'int'>, {}))

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_defaultdict.py:15: AssertionError
________________ test_valid_case_defaultdict[test_input3-True] _________________

test_input = {}, expected = True

    @pytest.mark.parametrize("test_input, expected", [
        (defaultdict(int), True),
        (dict, True),
        ([], False),
        ({}, True),  # Adding a test case for dict-like object
        ((), False),   # Adding a test case for tuple which is not a mapping
    ])
    def test_valid_case_defaultdict(test_input, expected):
>       assert _is_mapping(test_input) == expected
E       assert False == True
E        +  where False = _is_mapping({})

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_defaultdict.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_defaultdict.py::test_valid_case_defaultdict[test_input0-True]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_defaultdict.py::test_valid_case_defaultdict[test_input3-True]
========================= 2 failed, 3 passed in 0.04s ==========================

"""