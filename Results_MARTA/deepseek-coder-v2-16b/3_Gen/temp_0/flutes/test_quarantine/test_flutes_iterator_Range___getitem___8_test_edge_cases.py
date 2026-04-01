
import pytest
from flutes.iterator import Range

def test_edge_cases():
    # Test cases for edge cases in the range class
    r = Range(10)
    assert r[0] == 0, "Indexing at 0 should return 0"
    assert r[9] == 9, "Indexing at 9 (last element) should return 9"
    
    # Test for out of bounds index
    with pytest.raises(IndexError):
        r[10]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___8_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test cases for edge cases in the range class
        r = Range(10)
        assert r[0] == 0, "Indexing at 0 should return 0"
        assert r[9] == 9, "Indexing at 9 (last element) should return 9"
    
        # Test for out of bounds index
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___8_test_edge_cases.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___8_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.13s ===============================
"""