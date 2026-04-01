
import pytest
from dataclasses import dataclass
from typing import List, Union

# Assuming _get_type_origin and is_dataclass are defined in a module or utility file that we can mock here
def _get_type_origin(type_):
    # Mock implementation for testing purposes
    if isinstance(type_, type) and hasattr(type_, '__origin__'):
        return type_.__origin__
    return None

def is_dataclass(cls):
    # Mock implementation for testing purposes
    return hasattr(cls, '__dataclass_fields__')

# Import the function to be tested from its module or utility file
from dataclasses_json.utils import _is_generic_dataclass

@pytest.mark.parametrize("type_, expected", [
    (List[int], True),  # List is a generic and int is a dataclass
    (Union[int, str], False),  # Union is not a dataclass but both elements are
    (List[str], True),  # List is a generic and str is a dataclass
    (int, False),  # int is not a generic class
])
def test_is_generic_dataclass(type_, expected):
    assert _is_generic_dataclass(type_) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case.py F [ 25%]
.F.                                                                      [100%]

=================================== FAILURES ===================================
____________________ test_is_generic_dataclass[List-True0] _____________________

type_ = typing.List[int], expected = True

    @pytest.mark.parametrize("type_, expected", [
        (List[int], True),  # List is a generic and int is a dataclass
        (Union[int, str], False),  # Union is not a dataclass but both elements are
        (List[str], True),  # List is a generic and str is a dataclass
        (int, False),  # int is not a generic class
    ])
    def test_is_generic_dataclass(type_, expected):
>       assert _is_generic_dataclass(type_) == expected
E       assert False == True
E        +  where False = _is_generic_dataclass(typing.List[int])

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case.py:27: AssertionError
____________________ test_is_generic_dataclass[List-True1] _____________________

type_ = typing.List[str], expected = True

    @pytest.mark.parametrize("type_, expected", [
        (List[int], True),  # List is a generic and int is a dataclass
        (Union[int, str], False),  # Union is not a dataclass but both elements are
        (List[str], True),  # List is a generic and str is a dataclass
        (int, False),  # int is not a generic class
    ])
    def test_is_generic_dataclass(type_, expected):
>       assert _is_generic_dataclass(type_) == expected
E       assert False == True
E        +  where False = _is_generic_dataclass(typing.List[str])

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case.py::test_is_generic_dataclass[List-True0]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_edge_case.py::test_is_generic_dataclass[List-True1]
========================= 2 failed, 2 passed in 0.04s ==========================
"""