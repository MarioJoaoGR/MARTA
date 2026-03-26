
import pytest
from flutes.structure import map_structure
from typing import Callable, Collection, TypeVar

T = TypeVar('T')
R = TypeVar('R')

# Assuming _NO_MAP_TYPES and _NO_MAP_INSTANCE_ATTR are defined in the module 'flutes.structure'
# from flutes.structure import _NO_MAP_TYPES, _NO_MAP_INSTANCE_ATTR

def test_invalid_inputs():
    with pytest.raises(TypeError):
        map_structure(lambda x: x ** 2, 123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_invalid_inputs.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""