
import pytest
from typing import Tuple, Union
from dataclasses_json.utils import _NO_ARGS, _get_type_args

# Test cases for _get_type_args function
def test_get_type_args_with_no_args():
    from typing import List
    tp = List[int]
    result = _get_type_args(tp)
    assert result == ()

def test_get_type_args_without_default():
    from typing import Tuple
    tp = Tuple[int, str]
    result = _get_type_args(tp)
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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_1.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_get_type_args_with_no_args ________________________

    def test_get_type_args_with_no_args():
        from typing import List
        tp = List[int]
        result = _get_type_args(tp)
>       assert result == ()
E       AssertionError: assert (<class 'int'>,) == ()
E         
E         Left contains one more item: <class 'int'>
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_1.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_1.py::test_get_type_args_with_no_args
========================= 1 failed, 1 passed in 0.02s ==========================

"""