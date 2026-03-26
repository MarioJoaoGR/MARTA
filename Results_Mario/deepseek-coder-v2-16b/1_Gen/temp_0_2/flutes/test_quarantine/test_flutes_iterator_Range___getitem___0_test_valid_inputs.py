
import pytest
from flutes.iterator import Range

def test_valid_inputs():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
    
    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5
    
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5

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

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        r = Range(10)
        assert r[0] == 0
        assert r[2] == 2
        assert r[4] == 4
    
        r = Range(1, 10 + 1)
        assert r[0] == 1
        assert r[2] == 3
        assert r[4] == 5
    
        r = Range(1, 11, 2)
        assert r[0] == 1
>       assert r[2] == 3
E       assert 5 == 3

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""