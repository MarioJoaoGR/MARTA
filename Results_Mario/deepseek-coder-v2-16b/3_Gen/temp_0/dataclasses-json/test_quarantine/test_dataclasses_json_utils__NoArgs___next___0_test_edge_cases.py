
from dataclasses_json.utils import NoArgs
import pytest

def test_function_name():
    with pytest.raises(StopIteration):
        instance = _NoArgs()
        next(instance)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__NoArgs___next___0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__NoArgs___next___0_test_edge_cases.py:2:0: E0611: No name 'NoArgs' in module 'dataclasses_json.utils' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__NoArgs___next___0_test_edge_cases.py:7:19: E0602: Undefined variable '_NoArgs' (undefined-variable)


"""