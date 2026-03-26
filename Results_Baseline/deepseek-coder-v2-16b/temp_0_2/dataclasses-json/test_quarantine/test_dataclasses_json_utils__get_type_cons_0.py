
import pytest
import sys
from typing import List, Dict, Union

# Import the function from its module
from dataclasses_json.utils import _get_type_origin as get_type_cons

class MyCustomType:
    pass

@pytest.mark.parametrize("type_, expected", [
    (List[int], list),  # Test with a generic type (list of int)
    (Dict[str, str], dict),  # Test with another generic type (dict of str to str)
    (Union[int, str], None),  # Test with a built-in type without __origin__ in Python 3.6 and 3.7
    (MyCustomType, MyCustomType.__class__ if sys.version_info.minor == 6 else None),  # Test with a custom user-defined type
])
def test_get_type_cons(type_, expected):
    if sys.version_info.minor == 6:
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_cons_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0.py:19:36: E0001: Parsing failed: 'expected an indented block after 'if' statement on line 19 (Test4DT_tests.test_dataclasses_json_utils__get_type_cons_0, line 19)' (syntax-error)

"""