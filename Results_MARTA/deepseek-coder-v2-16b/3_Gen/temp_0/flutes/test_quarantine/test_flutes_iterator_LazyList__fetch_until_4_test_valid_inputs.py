
import pytest
from flutes.iterator import LazyList

def test_valid_inputs():
    # Test with a valid list
    lst = LazyList([1, 2, 3, 4])
    assert isinstance(lst, LazyList)
    
    # Check the length of the list after fetching until index 3
    lst._fetch_until(3)
    assert len(lst.list) == 4
    
    # Check if elements are fetched correctly
    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == 3
    assert lst[3] == 4
    
    # Test fetching until a specific index that is out of bounds
    with pytest.raises(StopIteration):
        lst._fetch_until(5)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_4_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with a valid list
        lst = LazyList([1, 2, 3, 4])
        assert isinstance(lst, LazyList)
    
        # Check the length of the list after fetching until index 3
        lst._fetch_until(3)
        assert len(lst.list) == 4
    
        # Check if elements are fetched correctly
        assert lst[0] == 1
        assert lst[1] == 2
        assert lst[2] == 3
        assert lst[3] == 4
    
        # Test fetching until a specific index that is out of bounds
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_4_test_valid_inputs.py:21: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_4_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================

"""