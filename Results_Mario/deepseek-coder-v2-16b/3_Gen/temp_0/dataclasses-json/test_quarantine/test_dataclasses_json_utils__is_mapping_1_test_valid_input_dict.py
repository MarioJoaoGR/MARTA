
from collections import defaultdict
from typing import Mapping
from dataclasses_json.utils import _get_type_origin, _issubclass_safe

def test_valid_input_dict():
    assert _is_mapping(dict) == True
    my_defaultdict = defaultdict(int)
    assert _is_mapping(my_defaultdict) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_1_test_valid_input_dict
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_1_test_valid_input_dict.py:7:11: E0602: Undefined variable '_is_mapping' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_1_test_valid_input_dict.py:9:11: E0602: Undefined variable '_is_mapping' (undefined-variable)


"""