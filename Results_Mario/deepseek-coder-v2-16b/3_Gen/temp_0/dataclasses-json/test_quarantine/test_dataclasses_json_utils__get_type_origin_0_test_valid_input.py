
import pytest
from dataclasses_json.utils import _get_type_origin, _NO_TYPE_ORIGIN
from typing import List, Union

def test_valid_input():
    # Test with a simple type
    my_list = List[int]
    assert _get_type_origin(my_list) == list
    
    # Test with a union type
    mixed_types = Union[int, str]
    assert _get_type_origin(mixed_types) in (int, str)
    
    # Additional test to ensure it handles None and special markers correctly
    class CustomType: pass
    custom_type = CustomType
    assert _get_type_origin(custom_type) == CustomType

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
        # Test with a simple type
        my_list = List[int]
        assert _get_type_origin(my_list) == list
    
        # Test with a union type
        mixed_types = Union[int, str]
>       assert _get_type_origin(mixed_types) in (int, str)
E       AssertionError: assert typing.Union in (<class 'int'>, <class 'str'>)
E        +  where typing.Union = _get_type_origin(typing.Union[int, str])

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""