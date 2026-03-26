
import pytest
from dataclasses_json.utils import _get_type_origin, _NO_TYPE_ORIGIN
from typing import List, Union
import sys

@pytest.mark.parametrize("input_type, expected", [
    (None, None),
    (List[int], List),
    (Union[int, str], Union)
])
def test_get_type_origin(input_type, expected):
    result = _get_type_origin(input_type)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_none_input.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_get_type_origin[List-List] ________________________

input_type = typing.List[int], expected = typing.List

    @pytest.mark.parametrize("input_type, expected", [
        (None, None),
        (List[int], List),
        (Union[int, str], Union)
    ])
    def test_get_type_origin(input_type, expected):
        result = _get_type_origin(input_type)
>       assert result == expected
E       AssertionError: assert <class 'list'> == typing.List

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_none_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_none_input.py::test_get_type_origin[List-List]
========================= 1 failed, 2 passed in 0.05s ==========================
"""