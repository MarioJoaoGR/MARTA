
import pytest
from flutes.iterator import Range

def test_valid_case_three_arguments():
    r = Range(1, 10, 2)
    assert isinstance(r, Range), "Instance should be of type Range"
    assert r.l == 1, "Start value should be 1"
    assert r.r == 10, "Stop value should be 10"
    assert r.step == 2, "Step value should be 2"
    assert r.length == (10 - 1) // 2, "Length calculation is incorrect"

    # Check indexing
    assert r[0] == 1, "Indexing error: expected 1 but got something else"
    assert r[1] == 3, "Indexing error: expected 3 but got something else"
    assert r[2] == 5, "Indexing error: expected 5 but got something else"
    assert r[3] == 7, "Indexing error: expected 7 but got something else"
    assert r[4] == 9, "Indexing error: expected 9 but got something else"

    # Test negative indexing
    assert r[-1] == 9, "Negative indexing error: expected 9 but got something else"

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

flutes/Test4DT_tests/test_flutes_iterator_Range___init___1_test_valid_case_three_arguments.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_case_three_arguments ________________________

    def test_valid_case_three_arguments():
        r = Range(1, 10, 2)
        assert isinstance(r, Range), "Instance should be of type Range"
        assert r.l == 1, "Start value should be 1"
        assert r.r == 10, "Stop value should be 10"
        assert r.step == 2, "Step value should be 2"
        assert r.length == (10 - 1) // 2, "Length calculation is incorrect"
    
        # Check indexing
        assert r[0] == 1, "Indexing error: expected 1 but got something else"
        assert r[1] == 3, "Indexing error: expected 3 but got something else"
        assert r[2] == 5, "Indexing error: expected 5 but got something else"
        assert r[3] == 7, "Indexing error: expected 7 but got something else"
        assert r[4] == 9, "Indexing error: expected 9 but got something else"
    
        # Test negative indexing
>       assert r[-1] == 9, "Negative indexing error: expected 9 but got something else"
E       AssertionError: Negative indexing error: expected 9 but got something else
E       assert 7 == 9

flutes/Test4DT_tests/test_flutes_iterator_Range___init___1_test_valid_case_three_arguments.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___1_test_valid_case_three_arguments.py::test_valid_case_three_arguments
============================== 1 failed in 0.10s ===============================
"""