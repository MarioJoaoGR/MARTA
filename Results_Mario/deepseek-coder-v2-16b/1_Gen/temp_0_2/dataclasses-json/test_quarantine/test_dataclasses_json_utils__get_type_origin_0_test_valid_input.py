
import pytest
from dataclasses_json.utils import _get_type_origin, _NO_TYPE_ORIGIN
from typing import List
import sys

def test_valid_input():
    my_list = List[int]
    origin = _get_type_origin(my_list)
    assert origin == list
    
    # Additional tests for different versions and types
    if sys.version_info.minor == 6:
        assert _get_type_origin(List[int]).__extra__ == list
    else:
        assert _get_type_origin(List[int]).__origin__ == list

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        my_list = List[int]
        origin = _get_type_origin(my_list)
        assert origin == list
    
        # Additional tests for different versions and types
        if sys.version_info.minor == 6:
            assert _get_type_origin(List[int]).__extra__ == list
        else:
>           assert _get_type_origin(List[int]).__origin__ == list
E           AttributeError: type object 'list' has no attribute '__origin__'

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input.py:16: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""