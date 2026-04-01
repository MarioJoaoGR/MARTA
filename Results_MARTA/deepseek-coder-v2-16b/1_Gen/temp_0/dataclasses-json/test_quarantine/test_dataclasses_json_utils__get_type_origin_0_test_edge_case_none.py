
import pytest
from dataclasses_json.utils import _get_type_origin
from typing import List, Union

def test_edge_case_none():
    # Test when the type has no origin (should return the type itself)
    my_list = List[int]
    assert _get_type_origin(my_list) == List[int]

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        # Test when the type has no origin (should return the type itself)
        my_list = List[int]
>       assert _get_type_origin(my_list) == List[int]
E       AssertionError: assert <class 'list'> == typing.List[int]
E        +  where <class 'list'> = _get_type_origin(typing.List[int])

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_edge_case_none.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.03s ===============================

"""