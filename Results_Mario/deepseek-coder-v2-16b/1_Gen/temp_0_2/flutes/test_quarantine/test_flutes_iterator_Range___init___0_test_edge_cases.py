
import pytest
from flutes.iterator import Range

def test_range_init():
    # Test with one argument (end)
    r = Range(10)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.length == 10
    
    # Test with two arguments (start and end)
    r = Range(1, 10 + 1)
    assert r.l == 1
    assert r.r == 10
    assert r.step == 1
    assert r.length == 10
    
    # Test with three arguments (start, end, and step)
    r = Range(1, 11, 2)
    assert r.l == 1
    assert r.r == 11
    assert r.step == 2
    assert r.length == 5

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

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_range_init ________________________________

    def test_range_init():
        # Test with one argument (end)
        r = Range(10)
        assert r.l == 0
        assert r.r == 10
        assert r.step == 1
        assert r.length == 10
    
        # Test with two arguments (start and end)
        r = Range(1, 10 + 1)
        assert r.l == 1
>       assert r.r == 10
E       assert 11 == 10
E        +  where 11 = <flutes.iterator.Range object at 0x7f424fada3d0>.r

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_edge_cases.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_edge_cases.py::test_range_init
============================== 1 failed in 0.09s ===============================
"""