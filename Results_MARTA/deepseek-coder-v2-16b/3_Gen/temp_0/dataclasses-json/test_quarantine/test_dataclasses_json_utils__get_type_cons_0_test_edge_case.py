
import pytest
from dataclasses_json.utils import _get_type_cons
from typing import Union, List

def test_edge_case():
    my_list = [1, 2, 3]
    cons = _get_type_cons(my_list.__class__)
    assert isinstance(cons, type)
    if sys.version_info.minor == 6:
        assert cons in (List, Union)
    else:
        assert cons == List

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_cons_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0_test_edge_case.py:10:7: E0602: Undefined variable 'sys' (undefined-variable)


"""