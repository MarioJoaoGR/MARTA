
import pytest
from flutes.iterator import Range

def test_valid_inputs():
    # Test with one argument (end value)
    r = Range(10)
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Test with two arguments (start and end)
    r = Range(1, 10 + 1)
    assert list(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Test with three arguments (start, end, and step)
    r = Range(1, 11, 2)
    assert list(r) == [1, 3, 5, 7, 9]
    
    # Test with negative values for start, end, and step
    r = Range(0, -10, -1)
    assert list(r) == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

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

flutes/Test4DT_tests/test_flutes_iterator_Range___next___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with one argument (end value)
        r = Range(10)
        assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
        # Test with two arguments (start and end)
        r = Range(1, 10 + 1)
        assert list(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
        # Test with three arguments (start, end, and step)
        r = Range(1, 11, 2)
        assert list(r) == [1, 3, 5, 7, 9]
    
        # Test with negative values for start, end, and step
        r = Range(0, -10, -1)
>       assert list(r) == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
E       assert [] == [0, -1, -2, -3, -4, -5, ...]
E         
E         Right contains 10 more items, first extra item: 0
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_Range___next___0_test_valid_inputs.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___next___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""