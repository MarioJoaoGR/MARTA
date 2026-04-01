
from dataclasses_json.utils import _get_type_args, _NO_ARGS
from typing import Tuple, Type, Union, Generic, TypeVar

def test_no_arguments_provided():
    tp = Tuple
    result = _get_type_args(tp)
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
__________________________ test_no_arguments_provided __________________________

    def test_no_arguments_provided():
        tp = Tuple
        result = _get_type_args(tp)
>       assert result == ()
E       assert <dataclasses_...t 0x105ba51e0> == ()
E         
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_0_test_valid_input_with_args.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_0_test_valid_input_with_args.py::test_no_arguments_provided
============================== 1 failed in 0.03s ===============================
"""