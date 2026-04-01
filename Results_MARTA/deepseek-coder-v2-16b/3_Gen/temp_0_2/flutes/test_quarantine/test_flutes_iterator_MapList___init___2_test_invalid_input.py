
import pytest
from flutes.iterator import MapList
from typing import Callable, Sequence, Any

def test_invalid_input():
    # Test that MapList raises a TypeError when func is not callable or lst is not a sequence
    
    # Invalid function input (not callable)
    with pytest.raises(TypeError):
        MapList("not_a_function", [1, 2, 3])

    # Invalid list input (not a sequence)
    with pytest.raises(TypeError):
        MapList(lambda x: x * x, "not_a_sequence")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_MapList___init___2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test that MapList raises a TypeError when func is not callable or lst is not a sequence
    
        # Invalid function input (not callable)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_iterator_MapList___init___2_test_invalid_input.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_MapList___init___2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""