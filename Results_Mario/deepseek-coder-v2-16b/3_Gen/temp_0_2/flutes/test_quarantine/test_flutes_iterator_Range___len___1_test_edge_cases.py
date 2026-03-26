
import pytest
from flutes.iterator import Range

def test_edge_cases():
    # Test case 1: Creating a range with one argument (end)
    r = Range(10)
    assert len(r) == 10
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

    # Test case 2: Creating a range with two arguments (start and end)
    r = Range(1, 10 + 1)
    assert len(r) == 10
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5

    # Test case 3: Creating a range with three arguments (start, end, and step)
    r = Range(1, 11, 2)
    assert len(r) == 5
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9

    # Test case 4: Creating a range with invalid number of arguments
    with pytest.raises(ValueError):
        Range()
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

    # Test case 5: Accessing elements out of bounds
    r = Range(1, 10 + 1)
    with pytest.raises(IndexError):
        r[10]

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

flutes/Test4DT_tests/test_flutes_iterator_Range___len___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test case 1: Creating a range with one argument (end)
        r = Range(10)
        assert len(r) == 10
        assert r[0] == 0
        assert r[2] == 2
        assert r[4] == 4
    
        # Test case 2: Creating a range with two arguments (start and end)
        r = Range(1, 10 + 1)
        assert len(r) == 10
        assert r[0] == 1
        assert r[2] == 3
        assert r[4] == 5
    
        # Test case 3: Creating a range with three arguments (start, end, and step)
        r = Range(1, 11, 2)
        assert len(r) == 5
        assert r[0] == 1
        assert r[2] == 5
        assert r[4] == 9
    
        # Test case 4: Creating a range with invalid number of arguments
        with pytest.raises(ValueError):
            Range()
        with pytest.raises(ValueError):
            Range(1, 2, 3, 4)
    
        # Test case 5: Accessing elements out of bounds
        r = Range(1, 10 + 1)
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___len___1_test_edge_cases.py:35: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___len___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""