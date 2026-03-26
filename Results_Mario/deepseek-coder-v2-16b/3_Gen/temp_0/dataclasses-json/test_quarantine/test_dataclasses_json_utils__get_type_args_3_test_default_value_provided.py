
import pytest
from dataclasses_json.utils import _get_type_args, _NO_ARGS
from typing import Tuple, Type, Union

def test_default_value_provided():
    # Test when the type is a generic type and a specific default value is provided
    result = _get_type_args(Tuple[int, str], (str,))
    assert result == (str,)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_3_test_default_value_provided.py F [100%]

=================================== FAILURES ===================================
_________________________ test_default_value_provided __________________________

    def test_default_value_provided():
        # Test when the type is a generic type and a specific default value is provided
        result = _get_type_args(Tuple[int, str], (str,))
>       assert result == (str,)
E       AssertionError: assert (<class 'int'>, <class 'str'>) == (<class 'str'>,)
E         
E         At index 0 diff: <class 'int'> != <class 'str'>
E         Left contains one more item: <class 'str'>
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_3_test_default_value_provided.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_3_test_default_value_provided.py::test_default_value_provided
============================== 1 failed in 0.03s ===============================
"""