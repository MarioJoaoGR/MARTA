
import pytest
from dataclasses_json.utils import _get_type_origin, _NO_TYPE_ORIGIN
from typing import List, Type
from collections import deque
import sys

def test_valid_case_python36():
    # Test case for Python 3.6
    class MyDeque(deque): pass
    
    my_list = List[int]
    assert _get_type_origin(my_list) == list
    
    my_deque = MyDeque()  # Assuming MyDeque is a subclass of deque
    assert _get_type_origin(my_deque) == deque

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_case_python36.py F [100%]

=================================== FAILURES ===================================
___________________________ test_valid_case_python36 ___________________________

    def test_valid_case_python36():
        # Test case for Python 3.6
        class MyDeque(deque): pass
    
        my_list = List[int]
        assert _get_type_origin(my_list) == list
    
        my_deque = MyDeque()  # Assuming MyDeque is a subclass of deque
>       assert _get_type_origin(my_deque) == deque
E       assert MyDeque([]) == deque
E        +  where MyDeque([]) = _get_type_origin(MyDeque([]))

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_case_python36.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_case_python36.py::test_valid_case_python36
============================== 1 failed in 0.02s ===============================
"""