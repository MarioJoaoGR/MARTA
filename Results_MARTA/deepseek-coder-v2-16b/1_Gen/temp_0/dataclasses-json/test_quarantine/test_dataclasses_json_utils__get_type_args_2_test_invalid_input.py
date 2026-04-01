
import pytest
from dataclasses_json.utils import _get_type_args, _NO_ARGS
from typing import Tuple, Type, Union

def test_invalid_input():
    # Test with a non-generic type (should return the default value)
    result = _get_type_args(int)
    assert result == _NO_ARGS
    
    # Test with None as the input type (should return the default value)
    result_none = _get_type_args(None)
    assert result_none == _NO_ARGS
    
    # Test with a specific default value provided
    result_with_default = _get_type_args(Tuple[int, str], (str,))
    assert result_with_default == (str,)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with a non-generic type (should return the default value)
        result = _get_type_args(int)
        assert result == _NO_ARGS
    
        # Test with None as the input type (should return the default value)
        result_none = _get_type_args(None)
        assert result_none == _NO_ARGS
    
        # Test with a specific default value provided
        result_with_default = _get_type_args(Tuple[int, str], (str,))
>       assert result_with_default == (str,)
E       AssertionError: assert (<class 'int'>, <class 'str'>) == (<class 'str'>,)
E         
E         At index 0 diff: <class 'int'> != <class 'str'>
E         Left contains one more item: <class 'str'>
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_2_test_invalid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================

"""