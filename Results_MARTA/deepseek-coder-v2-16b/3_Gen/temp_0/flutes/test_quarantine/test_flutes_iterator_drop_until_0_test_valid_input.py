
import pytest
from flutes.iterator import drop_until

def test_valid_input():
    # Test case where the predicate is satisfied after some elements
    result = list(drop_until(lambda x: x > 5, range(10)))
    assert result == [6, 7, 8, 9]
    
    # Test case where all elements satisfy the predicate
    result = list(drop_until(lambda x: x < 0, range(10)))
    assert result == []
    
    # Test case where the first element satisfies the predicate
    result = list(drop_until(lambda x: x > -1, [-2, -1, 0, 1]))
    assert result == [-1, 0, 1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_drop_until_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test case where the predicate is satisfied after some elements
        result = list(drop_until(lambda x: x > 5, range(10)))
        assert result == [6, 7, 8, 9]
    
        # Test case where all elements satisfy the predicate
        result = list(drop_until(lambda x: x < 0, range(10)))
        assert result == []
    
        # Test case where the first element satisfies the predicate
        result = list(drop_until(lambda x: x > -1, [-2, -1, 0, 1]))
>       assert result == [-1, 0, 1]
E       assert [0, 1] == [-1, 0, 1]
E         
E         At index 0 diff: 0 != -1
E         Right contains one more item: 1
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_drop_until_0_test_valid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_drop_until_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""