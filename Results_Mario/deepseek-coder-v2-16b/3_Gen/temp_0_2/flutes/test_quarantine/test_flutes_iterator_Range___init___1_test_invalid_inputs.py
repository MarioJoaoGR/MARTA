
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        Range()  # No arguments provided

    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)  # More than three arguments provided

    with pytest.raises(ValueError):
        Range(1)  # Only one argument provided (should be treated as stop)

    # Correct usage of the constructor:
    r = Range(10)         # Equivalent to range(10)
    assert isinstance(r, Range)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1

    r = Range(1, 10 + 1)  # Equivalent to range(1, 11)
    assert isinstance(r, Range)
    assert r.l == 1
    assert r.r == 11
    assert r.step == 1

    r = Range(1, 11, 2)   # Equivalent to range(1, 11, 2)
    assert isinstance(r, Range)
    assert r.l == 1
    assert r.r == 11
    assert r.step == 2

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

flutes/Test4DT_tests/test_flutes_iterator_Range___init___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            Range()  # No arguments provided
    
        with pytest.raises(ValueError):
            Range(1, 2, 3, 4)  # More than three arguments provided
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___init___1_test_invalid_inputs.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.10s ===============================
"""