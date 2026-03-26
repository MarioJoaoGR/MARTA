
from dataclasses_json.utils import _get_type_arg_param, _NO_ARGS
from typing import Type, Tuple, Union, cast
import pytest

def test_valid_input():
    from typing import Tuple
    
    # Test with a valid index
    result = _get_type_arg_param(Tuple[int, str], 0)
    assert isinstance(result, int), f"Expected int but got {type(result)}"
    
    # Test with an out-of-range index
    result_out_of_range = _get_type_arg_param(Tuple[int, str], 2)
    assert result_out_of_range is _NO_ARGS, f"Expected _NO_ARGS but got {result_out_of_range}"
    
    # Test with a specific default value (not applicable in this context)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        from typing import Tuple
    
        # Test with a valid index
        result = _get_type_arg_param(Tuple[int, str], 0)
>       assert isinstance(result, int), f"Expected int but got {type(result)}"
E       AssertionError: Expected int but got <class 'type'>
E       assert False
E        +  where False = isinstance(<class 'int'>, int)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""