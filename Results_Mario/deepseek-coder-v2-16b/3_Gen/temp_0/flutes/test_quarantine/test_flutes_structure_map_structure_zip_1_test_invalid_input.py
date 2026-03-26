
import pytest
from flutes.structure import map_structure_zip
from typing import Callable, Collection, Sequence, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_invalid_input():
    # Define a function that takes two arguments
    def add(a, b): return a + b
    
    # Test with invalid input: one element is a set which is not allowed
    objs = [[1, 2], {3, 4}]
    with pytest.raises(ValueError) as excinfo:
        map_structure_zip(add, objs)
    assert str(excinfo.value) == "Structures cannot contain `set` because it's unordered"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Define a function that takes two arguments
        def add(a, b): return a + b
    
        # Test with invalid input: one element is a set which is not allowed
        objs = [[1, 2], {3, 4}]
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_invalid_input.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""