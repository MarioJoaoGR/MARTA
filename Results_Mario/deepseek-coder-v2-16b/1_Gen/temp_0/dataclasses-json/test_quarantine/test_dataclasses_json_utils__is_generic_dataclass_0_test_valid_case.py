
import pytest
from dataclasses_json.utils import _is_generic_dataclass, _get_type_origin, is_dataclass
from typing import List, Union

def test_valid_case():
    # Test with a generic dataclass (List[int])
    my_list = List[int]
    assert _is_generic_dataclass(my_list) == True
    
    # Test with a non-generic type (int)
    an_int = int
    assert _is_generic_dataclass(an_int) == False
    
    # Test with another generic dataclass (Union[int, str])
    mixed_types = Union[int, str]
    assert _is_generic_dataclass(mixed_types) == True

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Test with a generic dataclass (List[int])
        my_list = List[int]
>       assert _is_generic_dataclass(my_list) == True
E       assert False == True
E        +  where False = _is_generic_dataclass(typing.List[int])

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================

"""