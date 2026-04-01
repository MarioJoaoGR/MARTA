
from flutes.iterator import Range

def test_edge_cases():
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
    assert r[2] == 5
    assert r[4] == 9
    
    # Test negative indices
    assert r[-1] == 9
    assert r[-3] == 7

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
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
        assert r[2] == 5
        assert r[4] == 9
    
        # Test negative indices
        assert r[-1] == 9
>       assert r[-3] == 7
E       assert 5 == 7

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___2_test_edge_cases.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___2_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.12s ===============================
"""