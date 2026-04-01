
import pytest
from typing import Callable, Collection

# Assuming map_structure is defined in a module named 'flutes.structure'
from flutes.structure import map_structure

def square(x):
    return x ** 2

test_data = [123, 'string', {'a': 'b'}]

@pytest.mark.parametrize("invalid_input", test_data)
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        map_structure(square, invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_invalid_inputs.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_inputs[123] ___________________________

invalid_input = 123

    @pytest.mark.parametrize("invalid_input", test_data)
    def test_invalid_inputs(invalid_input):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_invalid_inputs.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_6_test_invalid_inputs.py::test_invalid_inputs[123]
========================= 1 failed, 2 passed in 0.11s ==========================
"""