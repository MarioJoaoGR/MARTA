
import pytest
from flutes.iterator import Range

def test_valid_inputs():
    # Test initialization with one argument (end)
    r1 = Range(10)
    assert r1[0] == 0
    assert len(r1) == 10
    
    # Test initialization with two arguments (start and end)
    r2 = Range(1, 10 + 1)
    assert r2[0] == 1
    assert r2[2] == 3
    assert len(r2) == 10
    
    # Test initialization with three arguments (start, end, and step)
    r3 = Range(1, 11, 2)
    assert r3[0] == 1
    assert r3[2] == 5
    assert len(r3) == 5
    
    # Additional test to ensure the range is inclusive at the end
    with pytest.raises(IndexError):
        r3[len(r3)]

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

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test initialization with one argument (end)
        r1 = Range(10)
        assert r1[0] == 0
        assert len(r1) == 10
    
        # Test initialization with two arguments (start and end)
        r2 = Range(1, 10 + 1)
        assert r2[0] == 1
        assert r2[2] == 3
        assert len(r2) == 10
    
        # Test initialization with three arguments (start, end, and step)
        r3 = Range(1, 11, 2)
        assert r3[0] == 1
        assert r3[2] == 5
        assert len(r3) == 5
    
        # Additional test to ensure the range is inclusive at the end
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_inputs.py:24: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""