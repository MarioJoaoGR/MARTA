
import pytest
from typing import Type, Tuple, Union, cast
from dataclasses_json.utils import _get_type_arg_param, _NO_ARGS

# Test cases for _get_type_arg_param function
def test_get_type_arg_param_valid_index():
    from typing import Tuple
    tp = Tuple[int, str]
    index = 0
    result = _get_type_arg_param(tp, index)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_get_type_arg_param_valid_index ______________________

    def test_get_type_arg_param_valid_index():
        from typing import Tuple
        tp = Tuple[int, str]
        index = 0
        result = _get_type_arg_param(tp, index)
>       assert isinstance(result, int), f"Expected type argument at index 0 to be int, but got {type(result)}"
E       AssertionError: Expected type argument at index 0 to be int, but got <class 'type'>
E       assert False
E        +  where False = isinstance(<class 'int'>, int)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_arg_param_0.py::test_get_type_arg_param_valid_index
========================= 1 failed, 1 passed in 0.03s ==========================

"""