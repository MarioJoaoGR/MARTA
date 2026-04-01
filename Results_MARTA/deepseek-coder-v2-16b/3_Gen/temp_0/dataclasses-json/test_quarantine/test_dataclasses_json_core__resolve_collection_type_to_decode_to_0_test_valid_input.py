
import pytest
from dataclasses_json.core import _resolve_collection_type_to_decode_to, _get_type_cons
from typing import List

def test_valid_input():
    my_list = [1, 2, 3]
    resolved_type = _resolve_collection_type_to_decode_to(my_list.__class__)
    
    # Check if the resolved type is correct for a list
    assert isinstance(resolved_type, type)
    assert resolved_type == List

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__resolve_collection_type_to_decode_to_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        my_list = [1, 2, 3]
        resolved_type = _resolve_collection_type_to_decode_to(my_list.__class__)
    
        # Check if the resolved type is correct for a list
        assert isinstance(resolved_type, type)
>       assert resolved_type == List
E       AssertionError: assert <class 'list'> == List

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__resolve_collection_type_to_decode_to_0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__resolve_collection_type_to_decode_to_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""