
import pytest
from dataclasses_json.utils import _get_type_args, _NO_ARGS
from typing import Tuple, Type, Union

def test_valid_input_with_args():
    # Test with a generic type having arguments
    result = _get_type_args(Tuple[int, str])
    assert result == (int, str)
    
    # Test without any arguments and default value provided
    result = _get_type_args(Tuple)
    assert result == ()

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_0_test_valid_input_with_args.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_input_with_args __________________________

    def test_valid_input_with_args():
        # Test with a generic type having arguments
        result = _get_type_args(Tuple[int, str])
        assert result == (int, str)
    
        # Test without any arguments and default value provided
        result = _get_type_args(Tuple)
>       assert result == ()
E       assert <dataclasses_...t 0x10616da80> == ()
E         
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_0_test_valid_input_with_args.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_0_test_valid_input_with_args.py::test_valid_input_with_args
============================== 1 failed in 0.03s ===============================
"""