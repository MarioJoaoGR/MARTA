
from collections import Mapping
import pytest
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe

def test_valid_case_dict():
    assert _is_mapping(dict) is True
    my_defaultdict = defaultdict(int)
    assert _is_mapping(my_defaultdict) is True
    assert _is_mapping([]) is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_0_test_valid_case_dict
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_dict.py:2:0: E0611: No name 'Mapping' in module 'collections' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0_test_valid_case_dict.py:8:21: E0602: Undefined variable 'defaultdict' (undefined-variable)


"""