
# Import necessary modules and functions for testing
from flutes.structure import register_no_map_class, _NO_MAP_TYPES
from typing import Type
import pytest

# Define a mock class that we will later register as non-mappable
class MyCustomContainer(list):
    pass

def test_invalid_input():
    # Attempt to register an invalid input type (None) and check if it raises the expected TypeError
    with pytest.raises(TypeError):
        register_no_map_class(None)
    
    # Register a valid non-mappable class and ensure it is added to _NO_MAP_TYPES
    register_no_map_class(MyCustomContainer)
    assert MyCustomContainer in _NO_MAP_TYPES

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Attempt to register an invalid input type (None) and check if it raises the expected TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_invalid_input.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""